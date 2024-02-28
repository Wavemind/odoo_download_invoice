# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import base64

class AccountMove(models.Model):
    _name = 'account.move'
    _inherit = ['account.move']

    @api.model
    def download_pdf(self, *args, **kwargs):
        order_display_name = f'WOO{args[0]}'
        

        # Find the invoices linked to the sale order by its display name
        invoices = self.env['account.move'].search([
            ('invoice_origin', '=', order_display_name),
        ])

        return base64.b64encode(self.env['ir.actions.report']._render('account.account_invoices', invoices.ids)[0]) 