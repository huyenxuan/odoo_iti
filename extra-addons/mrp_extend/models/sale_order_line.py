from odoo import models, fields, api, _

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    technical_drawing_ids = fields.Many2many('drawing.technical', string='Drawing tecnical', tracking=True)
    
    # Post a message when technical_drawing_ids is changed
    def write(self, vals):
        for rec in self:
            before_set = set(rec.technical_drawing_ids.ids)
            res = super().write(vals)
            after_set = set(rec.technical_drawing_ids.ids)

            added_ids = after_set - before_set
            removed_ids = before_set - after_set

            messages = []
            if added_ids:
                added_names = self.env['drawing.technical'].browse(list(added_ids)).mapped("name")
                messages.append(_("Added drawing technical: %s in Product name: %s") % (', '.join(added_names), rec.name))
            if removed_ids:
                removed_names = self.env['drawing.technical'].browse(list(removed_ids)).mapped("name")
                messages.append(_("Removed drawing technical: %s in Product name: %s") % (', '.join(removed_names), rec.name))

            if messages and rec.order_id:
                rec.order_id.message_post(body="<br/>".join(messages))
        return res
    
    def action_create_drawing_technical(self):
        return {
            'name': 'Create Technical Drawing',
            'type': 'ir.actions.act_window',
            'res_model': 'drawing.technical',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_order_line_id': self.id,
            },
        }