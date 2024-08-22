{
    'name': "Vertical Hospitales",

    'summary': """
        Prueba tecnica Mateo""",

    'description': """
        Prueba tecnica Mateo
    """,

    'author': "Mateo Zabala",
    'website': "https://www.linkedin.com/in/mzabala1/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': [
        'base', 'mail',
    ],

    # always loaded
    'data': [
        'data/paciente_sequences.xml',
        'security/ir.model.access.csv',
        'views/paciente.xml',
        'views/tratamiento.xml',
        'views/hospital_config_view.xml',
        'reports/report_pacientes.xml',
    ],
    'application': True,
    'installable': True,
}
# -*- coding: utf-8 -*-

