# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp.osv import osv

class res_users(osv.osv):
    _inherit = 'res.users'

    def fields_get(self, cr, uid, fields=None, context=None):
        fields_to_hide = ['login', 'lang', 'image', 'action_id', 'alias_contact',
                          'alias_defaults', 'alias_domain', 'alias_force_thread_id',
                          'alias_id', 'alias_model_id', 'alias_name', 'alias_parent_model_id',
                          'alias_parent_thread_id', 'alias_user_id', 'bank_account_count',
                          'bank_ids', 'barcode', 'birthdate', 'channel_ids', 'chatter_needaction_auto',
                          'child_ids', 'color',
                          'commercial_partner_id',
                          'company_id', 'company_ids',
                          'company_type', 'contract_ids', 'contracts_count', 'country_id', 'create_date',
                          'create_uid', 'credit', 'credit_limit', 'currency_id', 'debit', 'debit_limit',
                          'employee', 'fax', 'function', 'groups_id', 'has_unreconciled_entries',
                          'id', 'image_medium', 'image_small', 'im_status', 'invoice_ids', 'is_company',
                          'issued_total', 'journal_item_count', '__last_update',
                          'message_follower_ids', 'message_needaction', 'message_needaction_counter',
                          'message_partner_ids',
                          'message_unread', 'message_unread_counter', 'new_password',
                          'notify_email', 'opt_out', 'parent_id', 'parent_name',
                          'partner_id', 'message_channel_ids', 'message_is_follower', 'active', 'date',
                          'message_last_post', 'city', 'log_ids', 'password_crypt', 'password', 'pos_security_pin',
                          'share', 'signature',

                          # common fields
                          'write_uid', 'write_date',

                          # parent partner fields
                          'zip',
                          'bank_account_count', 'bank_ids', 'barcode', 'color', 'commercial_partner_id', 'customer',
                          'company_id', 'company_type', 'contract_ids', 'contracts_count', 'country_id',
                          'create_date', 'create_uid', 'credit_limit', 'currency_id', 'credit', 'credit_limit',
                          'debit', 'debit_limit', 'fax', 'has_unreconciled_entries', 'image',
                          'image_medium', 'image_small', 'im_status', 'invoice_ids', 'journal_item_count',
                          'lang', 'last_time_entries_checked', '__last_update', 'message_needaction',
                          'message_needaction_counter', 'message_unread', 'message_unread_counter', 'notify_email',
                          'opt_out', 'parent_id', 'parent_name', 'payment_method_count', 'payment_method_ids',
                          'property_account_payable_id', 'property_account_position_id',
                          'property_account_receivable_id',
                          'property_payment_term_id', 'property_product_pricelist', 'property_stock_customer',
                          'property_stock_supplier', 'property_supplier_payment_term_id', 'ref', 'ref_company_ids',
                          'sale_order_count', 'sale_order_ids', 'signup_expiration', 'signup_token', 'signup_type',
                          'signup_url', 'use_parent_address', 'website', 'user_ids', 'team_id', 'user_id', 'supplier',
                          'type', 'state_id', 'vat', 'tz', 'title'

                          ]  # you can set this dynamically
        res = super(res_users, self).fields_get(cr, uid, fields, context)
        for field in fields_to_hide:
            res[field]['selectable'] = False
        return res