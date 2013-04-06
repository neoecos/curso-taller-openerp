# -*- coding: utf-8 -*-
from osv import fields, osv
from random import randint, random
from datetime import datetime, timedelta

class mi_modulo_mi_tabla(osv.osv):
    _name = "mi_modulo.mi_tabla"
    _order= 'name'
    _columns = {
        'name': fields.char('nombre', size=255, required=True, help='Coloque el nombre aquí', select=1),
        'active': fields.boolean('activo'),
        'quantity': fields.integer('cantidad'),
        'date': fields.date('fecha'),
        'datetime': fields.datetime('fecha y hora'),
        'description': fields.text('descripcion'),
        'price': fields.float('precio', digits = (10,4)),
        'state': fields.selection([('draft','borrador'),('active','Activo'),('cancelled','Cancelado')], 'estado', required=True),
    }

    _sql_constraints = [
        ('unique_name','unique(name)','El nombre debe ser único'),
    ]

    def _check_date(self, cr, uid, ids, context = None):
        is_valid_date = False
        present = datetime.now()
        for obj in self.browse(cr,uid,ids,context=None):
            if not obj.date:
                continue

            date = datetime.strptime(obj.date, '%Y-%m-%d')

            if( (date.year >= present.year) and (present.month >= present.month) and 
                (date.day > present.day) ):
                is_valid_date = True

        return is_valid_date
    
    def _check_datetime(self, cr, uid, ids, context = None):
        is_valid_datetime = False
        present = datetime.now()
        ten_minutes = timedelta(minutes=10)
        for obj in self.browse(cr,uid,ids,context=None):
            if not obj.datetime:
                continue
            date_time = datetime.strptime(obj.datetime, '%Y-%m-%d %H:%M:%S')
            #Allow no more than 10 min between datetimes             
            if((present - ten_minutes) < date_time ):
                is_valid_datetime = True

        return is_valid_datetime

    _constraints = [
        (_check_date,'Fecha debe ser en el futuro',['date']),
        (_check_datetime,'No puede tener más de 10 minutos de diferencia',['datetime']),
    ]

    def _random_quantity(self, cr, uid, context = None):
        return randint(5,100)
    
    def _get_default_datetime(self, cr, uid, context = None):        
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    _defaults = {
         'active': True,
         'state': 'draft',
         'price': lambda *a: random(),
         'quantity': _random_quantity,
         'datetime' : _get_default_datetime,
    }
    
mi_modulo_mi_tabla()