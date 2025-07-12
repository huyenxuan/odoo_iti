# -*- coding: utf-8 -*-
{
    'name': "Manufacturing Extension",

    'summary': "Thêm chức năng quản lý bản vẽ kỹ thuật",

    'description': """
- Tạo mới 1 model quản lý bản vẽ kĩ thuật (Form tạo mới gửi lại sau), có đính kèm 

- Trên sale.order.line, cho phép người dùng tạo mới 1 file đính kèm bản vẽ kĩ thuật => hệ thống sẽ hiển thị pop-up cho nhập thông tin bản vẽ kĩ thuật và đính kèm file => lưu thông tin bản vẽ đính kèm trên sale.order.line

- Thêm 1 menu riêng bản vẽ kĩ thuật để có thể lọc nhóm, tìm kiếm nhanh các bản vẽ kĩ thuật
    """,

    'author': "NXH107",
    'website': "https://www.nxh107.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'mail', 'mrp', 'purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/mrp_production_wizard_views.xml',
        'views/drawing_technical_views.xml',
        'views/sale_order_line_views.xml',
        'views/mrp_production_views.xml',
        'views/mrp_extend_menus.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}

