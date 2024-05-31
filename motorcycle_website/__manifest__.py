# -*- coding: utf-8 -*-
{
    'name': "Motorcycle Website",

    'summary': "Compare Motorcycles on our Webpage",

    'description': """
Compare various motorcycles
    """,

    'author': "yavy-odoo",
    'website': "https://www.github.com/yavy-odoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Kawiil/Custom Modules',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'motorcycle_registry', 'motorcycle_stock'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}

