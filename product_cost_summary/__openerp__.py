# -*- coding: utf-8 -*-
# © 2016 ClearCorp
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Update Cost by Materials',
    'summary': 'Added the feature of recalculate cost based on materials'
               ' of the product and services included in the product.',
    'version': '8.0.1.0',
    'category': 'Manufacturing',
    'website': 'http://clearcorp.cr',
    'author': 'ClearCorp',
    'license': 'AGPL-3',
    'sequence': 10,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': [
        'base',
        'product',
        'mrp',
    ],
    'data': [
        "views/product_summary_view.xml",
    ],

}
