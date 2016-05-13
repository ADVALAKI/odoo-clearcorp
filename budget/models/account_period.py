# -*- coding: utf-8 -*-
# © 2016 ClearCorp
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp.osv import fields, osv, orm
from openerp.tools.translate import _

class accountPeriodclose(orm.Model):
    
    _inherit = "account.period.close"
    
    def data_save(self, cr, uid, ids, context=None):
        period_obj = self.pool.get('account.period')
        distribution_obj = self.pool.get('account.move.line.distribution')
        line_obj = self.pool.get('account.move.line')
        
        line_distribution = None
        
        for form in self.read(cr, uid, ids, context=context):
             if form['sure']:
                for id in context['active_ids']:
                    #Search period selected
                    period_to_close = period_obj.browse(cr, uid, [id], context=context)[0]
                    #Search all periods before period selected
                    period_list = period_obj.search(cr, uid, [('fiscalyear_id', '=', period_to_close.fiscalyear_id.id),('date_stop','<=',period_to_close.date_stop)])
                    #Search all move_lines that match with period list
                    move_line_list = line_obj.search(cr, uid, [('period_id','in',period_list)])
                    #Search if those lines have distribution percentage 100%
                    for line in line_obj.browse(cr, uid, move_line_list, context=context):
                        line_distribution_id = distribution_obj.search(cr, uid, [('account_move_line_id', '=', line.id)])
                        line_distribution_list = distribution_obj.browse(cr, uid, line_distribution_id, context=context)
                        for line_distribution in line_distribution_list:
                            if line_distribution.distribution_percentage < 100:
                                #Create a error that show line reference
                                raise osv.except_osv(_('Invalid Action!'),_("All entry lines must be distributed in a 100 percentage. " \
                                                        "The move line with reference: '%s' is not completely distributed") % (line.ref,))
        
        return super(accountPeriodclose, self).data_save(cr, uid, ids, context=context)                 