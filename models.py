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
    lote_id = fields.One2many(comodel_name='cerveceria.lote', inverse_name='cerveza_id', string="Lote")
    ingrediente_id = fields.Many2many(comodel_name='cerveceria.ingrediente', inverse_name='cerveza_id', string="Ingrediente")

class Lote(models.Model):
    _name = 'cerveceria.lote'
    _description = 'cerveceria.lote'

    fecha_inicio_produccion = fields.Date(string="Fecha de inicio de produccion")
    fecha_estimada_fin = fields.Date(string="Fecha estimada de fin")
    cantidad_producida = fields.Integer(string="Cantidad producida")
    estado = fields.Selection([
        ('En proceso', 'en proceso'),
        ('Completo', 'completo'),
        ('En espera de empaquetado', 'en espera de empaquetado'),
        ], string="Estado")
    cerveza_id = fields.Many2one(comodel_name='cerveceria.cerveza',inverse_name='lote_id', string="Cerveza")
    empaquetado_id = fields.Many2one(comodel_name='cerveceria.empaquetado',inverse_name='lote_id', string="Empaquetado")

class Ingrediente(models.Model):
    _name = 'cerveceria.ingrediente'
    _description = 'cerveceria.ingrediente'

    name = fields.Char(string="Nombre")
    tipo = fields.Selection([
        ('Malta', 'malta'),
        ('Lupulo', 'lupulo'),
        ('Levadura', 'levadura'),
        ('Agua', 'agua'),
        ('Otro', 'otro'),
        ], string="Tipo")
    cantidad_disponible = fields.Float(string="Cantidad disponible (kg/L)")
    cerveza_id = fields.Many2many(comodel_name='cerveceria.cerveza',inverse_name='ingrediente_id', string="Cerveza")

class Empaquetado(models.Model):
    _name = 'cerveceria.empaquetado'
    _description = 'cerveceria.empaquetado'

    fecha_empaquetado = fields.Date(string="Fecha de empaquetado")
    cantidad_empaquetada = fields.Integer(string="Cantidad empaquetada")
    lote_id = fields.One2many(comodel_name='cerveceria.lote',inverse_name='empaquetado_id', string="Lote")