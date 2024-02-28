# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import base64

class AccountMove(models.Model):
    _name = 'account.move'
    _inherit = ['account.move']

    @api.model
    def download_pdf(self, ref):
        # Find the invoices linked to the sale order by its display name
        invoices = self.env['account.move'].search([('ref', '=', ref[0])])
        return base64.b64encode(self.env['ir.actions.report']._render('account.account_invoices', invoices.ids)[0])

    @api.model
    def pdf_exists(self, ref):
        invoice = self.env['account.move'].search([('ref', '=', ref[0])])
        attachment = self.env['ir.attachment'].search([('res_model', '=', 'account.move'), ('res_id', '=', invoice.id)])
        return 0 if attachment else 1