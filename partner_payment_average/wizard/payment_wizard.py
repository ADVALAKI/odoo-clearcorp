# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Addons modules by CLEARCORP S.A.
#    Copyright (C) 2009-TODAY CLEARCORP S.A. (<http://clearcorp.co.cr>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api

class PaymentWizard(models.TransientModel):

    _name = 'partner.payment.average.payment.wizard'

    #@api.one
    @api.multi
    def print_report(self):
        
        if not self.partner_ids:
            self.partner_ids = self.env['res.partner'].search([('customer','=',True)])
        datas = {
             'model': 'res.partner',
             'form': [],
        }
        return self.env['report'].get_action(self.partner_ids,
            'partner_payment_average.report_payment_average', data=datas)

    period_start = fields.Many2one('account.period', string='Start Period', required=True)
    period_end = fields.Many2one('account.period', string='End Period', required=True)
    partner_ids = fields.Many2many('res.partner', string='Partners', domain=[('customer','=',True)])