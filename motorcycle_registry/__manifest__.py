{
    'name': 'Motorcycle Registry',
    'version': '0.0.1',
    'description': 'Motorcyle Registry',
    'summary': 'Manage Registration of Motorcycles',
    'author': 'yavy-odoo',
    'website': 'github.com/yavy-odoo',
    'license': 'LGPL-3',
    'category': 'Kawiil/Custom Modules',
    'depends': ['base'],
    'data': [
        'security/motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        'views/motorcycle_menuitems.xml',
    'demo': [
        'data/demo.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {
        },
    'icon': '/motorcycle_registry/static/description/icon.png',
}