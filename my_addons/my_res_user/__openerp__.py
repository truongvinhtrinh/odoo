# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Trinh res_user Customize',
    'version': '1.0',
    'category': 'Point Of Sale',
    'sequence': 8001,
    'summary': 'Trinh general customize',
    'description': """
    To:
    -- invisible in 2 fields in res_user view:
        Fields:
            login, lang
    """,
    'website': 'https://www.odoo.com',
    'depends': ['pos_restaurant'],
    'data': [
       # 'views/res_user_view.xml',
    ],
    'demo': [],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
