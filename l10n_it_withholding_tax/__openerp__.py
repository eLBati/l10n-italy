# -*- coding: utf-8 -*-
#
#
#    Copyright (C) 2012 Domsense srl (<http://www.domsense.com>)
#    Copyright (C) 2012-2013 Associazione OpenERP Italia
#    (<http://www.openerp-italia.org>).
#    Copyright (C) 2012-2014 Agile Business Group sagl
#    (<http://www.agilebg.com>)
#    @author Lorenzo Battistini <lorenzo.battistini@agilebg.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{
    'name': "Italian Localisation - Withholding tax",
    'version': '1.0',
    'category': 'Localisation/Italy',
    'description': """
Withholding tax for supplier invoices
=====================================


Configuration
=============

In accounting configuration you have to set
 - Withholding tax payment term
 - Payable account for withholding taxes to pay
 - Withholding tax journal

You have to set the flag 'Withholding Tax' in tax codes related to
withholding taxes
""",
    'author': "Odoo Italian Community,Odoo Community Association (OCA)",
    'website': 'http://www.odoo-italia.org',
    'license': 'AGPL-3',
    "depends": ['account_voucher_cash_basis'],
    "data": [
        'account_view.xml', ],
    "demo": [
        'account_demo.xml',
    ],
    'test': [
        'test/purchase_payment.yml',
    ],
    "active": False,
    "installable": True
}
