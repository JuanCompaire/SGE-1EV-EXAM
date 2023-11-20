from odoo import api, models, fields

class Cerveza(models.Model):
    _name = 'cerveceria.cerveza'
    _description = 'cerveza.cerveza'

    tipo = fields.Char(string="Tipo")
    name = fields.Char(string="Nombre")
    descripcion = fields.Char(string="Descripcion")
    cantidad_alcohol = fields.Float(string="Cantidad de alcohol (%)")
    precio_unidad = fields.Float(string="Precio por unidad")
    volumen_unidad = fields.Float(string="Volumen por unidad (ml)")
    cantidad_inventario = fields.Integer(string="Cantidad en inventario")
    disponible = fields.Boolean(string="Disponible")