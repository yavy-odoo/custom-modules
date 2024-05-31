# -*- coding: utf-8 -*-
{
    'name': "motorcycle_stock",

    'summary': "Manage Stock of Motorcycles",

    'description': """
Manage Stock of Motorcycles"
    """,

    'author': "yavy-odoo",
    'website': "https://www.github.com/yavy-odoo",
    'license': 'LGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Kawiil/Custom Modules',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'motorcycle_registry', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        "views/motorcycle_stock_menuitem.xml",
        "views/product_template_view_inherit.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}

