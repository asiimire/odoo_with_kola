{
    'name': 'National ID Application',
    'version': '1.0',
    'author': 'Asiimire Patricia',
    'summary': 'Process national ID applications',
    'sequence': -100,
    'description': """This module allows processing of national ID applications.""",
    'category': 'Human Resources',
    'website': 'hhttps://www.odoo.com/app/employees-features',
    'depends': ['base', 'mail', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/national_id_application_views.xml',
        'views/national_id_application_templates.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}