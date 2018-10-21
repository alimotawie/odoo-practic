# -*- coding: utf-8 -*-

from odoo import models, fields, api

class my_first_odoo_app(models.Model):
       project = None
       delivery= None
       _inherit= 'sale.order'

       appartementno= fields.Integer(" Appartement number #")
       appartementad = fields.Text("Appartement address")

class myapp_product_template(models.Model):

       _inherit = 'product.template'
       isdublex = fields.Boolean(" duplex")
       isvilla = fields.Boolean('villa')
       isstudio = fields.Boolean('studio')
       project_id = fields.Many2one("my_first_odoo_app.project", "developer name")
       delivery_id = fields.Many2one("my_first_odoo_app.delivery", "deadline")



class project(models.Model):

       _name = "my_first_odoo_app.project"

       name=fields.Text('developer name')
       size = fields.Integer('land size')
       deadline = fields.Many2one("my_first_odoo_app.project", "deadline")



class delivery(models.Model):

       _name = "my_first_odoo_app.delivery"

       name = fields.Date('deadline')



       # delivery_date=fields.Date('date')

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100