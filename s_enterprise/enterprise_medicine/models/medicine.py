# -*- coding: utf-8 -*-
import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class EnterpriseMedicine(models.AbstractModel):
    _name = 'enterprise.medicine'
    _description = 'Medicine'

    @api.model
    def inject_medicine(self):
        self.env.ref('mail.ir_cron_module_update_notification').sudo().write({'active': False})

        ir_config = self.env['ir.config_parameter'].sudo()
        expiration_date = '2100-01-01 00:00:00'
        ir_config.set_param('database.expiration_date', expiration_date)
        _logger.info(f'Update enterprise with expiration_date: {expiration_date}')
