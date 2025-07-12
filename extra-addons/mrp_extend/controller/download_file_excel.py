from odoo import http, _
from odoo.http import request
from odoo.modules import get_module_path
import os

class MrpProductionDownloadController(http.Controller):
    @http.route('/mrp_production/template_import_lines', type='http', auth='user')
    def download_template(self, **kwargs):
        file_template_url = os.path.join(
            get_module_path('mrp_extend'),
            'static/files/product_template.xlsx'
        )
        if not file_template_url:
            return None
        
        with open(file_template_url, 'rb') as f:
            file_content = f.read()
        
        return request.make_response(
            file_content,
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', 'attachment; filename="template.xlsx"'),
            ]
        )
        
