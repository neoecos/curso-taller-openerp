# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from osv import fields, osv

class mi_modulo_mi_tabla(osv.osv):
    _name = "mi_modulo.mi_tabla"
    _columns = {
        'name': fields.char('nombre', size=255, required=True, help='Coloque el nombre aquí', select=1),
        'active': fields.boolean('activo'),
        'quantity': fields.integer('cantidad'),
        'date': fields.date('fecha'),
        'datetime': fields.datetime('fecha y hora'),
        'description': fields.text('descripción'),
        'price': fields.float('precio', digits = (10,2)),
        'state': fields.selection([('draft','borrador'),('active','Activo'),('cancelled','Cancelado')], 'estado'),
    }
    
    def _get_default_datetime(self, cr, uid, context = None):        
        tenDays = timedelta(days=10)
        tenDaysAgo = datetime.now() - tenDays
        return tenDaysAgo.__str__()
        #return datetime.now().__str__()
    def _get_default_description(self, cr, uid, context = None):        
        return "Descripción vacía por defecto"
    _log_access = True
    _defaults = {'datetime' : _get_default_datetime,
                'description' : _get_default_description, }
    
    
mi_modulo_mi_tabla()