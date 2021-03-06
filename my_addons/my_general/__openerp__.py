# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Trinh General Customize',
    'version': '1.0',
    'category': 'Sales Management',
    'sequence': 8000,
    'summary': 'Trinh general customize',
    'description': """
    To:
    -- invisible in Product Form:
        Fields:
            invoicing_policy
            to_weight fields
        Tabs:
            Inventory tab
            Accounting
            Notes
    """,
    'website': 'https://www.odoo.com',
    'depends': ['point_of_sale', 'sale', 'product', 'account'],
    'data': [
        'views/sale_view.xml',
        'views/account_view.xml',
    ],
    'demo': [],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
