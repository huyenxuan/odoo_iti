from odoo import models, fields

class DrawingTechnical(models.Model):
    _name = 'drawing.technical'
    _description = 'Drawing Technical'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Drawing Name', required=True, tracking=True)
    product_id = fields.Many2one('product.product', string='Product', required=True, tracking=True)
    order_line_id = fields.Many2many('sale.order.line', string='Sale Order Line', tracking=True)
    attachment = fields.Binary(string='Attachment', attachment=True, tracking=True)
    attachment_filename = fields.Char(string='Attachment Filename', tracking=True)
    description = fields.Text(string='Description')
    date_created = fields.Date(string='Created Date', default=fields.Date.today)
