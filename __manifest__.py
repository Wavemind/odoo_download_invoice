# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Invoice PDF Download',
    'version': '1.0.0',
    'summary': 'Adds functionality to download PDFs for Account Moves',
    'sequence': 10,
    'description': """This module extends the account.move model to add a method for downloading PDFs of account moves. This is particularly useful for businesses that need to easily generate and distribute invoices in PDF format directly from their accounting records.""",
    'category': 'Accounting',
    'website': 'https://www.wavemind.ch',
    'license': 'LGPL-3',
    'author': 'Wavemind Sàrl',
    'depends': ['base', 'account'],
    'data': [
    ],
    'demo': [
    ],
    'installable': True,
    'application': False, 
    'auto_install': False,
}
