# -*- coding: utf-8 -*-

{
    'name': "Product Sale",
    'version': '1.0',
    'summary': "Product Sale",
    'sequence': 1,
    'description': """
        This module add product sales, report, labels.
    """,
    'author': "Michael Chambilla",
    'depends': [
        'product',
        'sale_management',
    ],
    'data': [
        'views/product_template_views.xml',
        
        'security/ir_model_access.xml',
    ],
    'installable': True,
    'license': 'LGPL-3'
}
