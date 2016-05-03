# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Trinh Web',
    'category': 'Hidden',
    'version': '1.0',
    'description':
        """
OpenERP Web core module.
========================

This module provides the core of the OpenERP Web Client.
        """,
    'depends': ['web'],
    'auto_install': False,
    'data': [
    ],
    'qweb' : [
        "static/src/xml/*.xml",
    ],
    'bootstrap': True, # load translations for login screen
}
