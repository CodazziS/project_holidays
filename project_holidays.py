from openerp.osv import fields, osv
import datetime


class project_holidays_test(osv.Model):
    _inherit = 'project.task'

    def _get_holidays(self, cr, uid, ids, field_name, arg, context):

        d_start = datetime.date(2014, 1, 1)
        d_end = datetime.date(2015, 1, 1)

        res = []
        x = self.pool.get('public.holidays.holidays').get_range(d_start, d_end)
        print x
        return res

    _columns = {
        'get_holidays': fields.function(_get_holidays,
        string="getholi",
        type="text"),
    }
