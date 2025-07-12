from odoo import models, fields, api, _
from datetime import timedelta
from odoo.exceptions import UserError

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    allow_create_rfq = fields.Boolean(
        string="Allow auto create RFQ",
        help="Check this to allow creating this MO even when raw materials are insufficient.")

    def _check_quantity(self):
        """Chức năng kiểm tra xem số lượng trong kho còn đủ để sản xuất hay không"""
        for line in self.move_raw_ids:
            if line.product_uom_qty > line.product_id.qty_available:
                subtraction = line.product_uom_qty - line.product_id.qty_available
                raise UserError(_(f"Materials '{line.product_id.display_name}' are missing.\n"
                                  f"Quantity is still in the warehouse: {line.product_id.qty_available}.\n"
                                  f"Quantity needed: {line.product_uom_qty}.\n"
                                  f"Missing: {subtraction}"))

    def action_confirm(self):
        for rec in self:
            if rec.allow_create_rfq:
                self._auto_create_rfq()
            else:
                self._check_quantity()
        return super().action_confirm()

    def _auto_create_rfq(self):
        """Chức năng tự động tạo đơn mua hàng (RFQ) khi nguyên liệu trong kho không đủ sau khi xác nhận MO"""
        purchase_order_obj = self.env['purchase.order']
        supplier_id = self.env['res.partner'].search([
            ('supplier_rank', '>', 0),
        ], limit=1)

        if not supplier_id:
            raise UserError(_("No supplier found"))
        
        order_lines = []
        for line in self.move_raw_ids:
            if line.product_uom_qty > line.product_id.qty_available:
                qty_order = line.product_uom_qty - line.product_id.qty_available
                order_lines.append((0, 0, {
                    'product_id': line.product_id.id,
                    'product_qty': qty_order,
                }))
        
        if order_lines:
            po = purchase_order_obj.create({
                'partner_id': supplier_id.id,
                'order_line': order_lines,
                'notes': _('Automatically order because of lack of raw materials.')
            })        
            self.message_post(body=_("Create RFQ %s beacause of lack of raw materials") % po.name)
