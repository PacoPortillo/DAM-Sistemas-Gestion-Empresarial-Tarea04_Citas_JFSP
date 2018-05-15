# -*- coding: utf-8 -*-

from odoo import models, fields, api

class citasjfsp(models.Model):
    # Nombre del modelo, que será también el mismo para la tabla de la base de datos:
    _name = 'citasjfsp.citasjfsp'
    # Métodos de ordenación:
    _order = 'fecha_visualizacion desc, orden desc'
     
    # Campos para los datos:
    cita = fields.Text(help='Escribe tu cita', required=True)
    autor = fields.Many2one('res.users', default = lambda self: self.env.user, help='Autor de la cita', required=True)
    fecha_visualizacion = fields.Date(default=fields.Date.today, help='Fecha para la cita', required=True)
    orden = fields.Integer('Prioridad:', help='A mayor número mayor prioridad', required=True)


