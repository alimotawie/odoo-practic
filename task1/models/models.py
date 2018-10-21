# -*- coding: utf-8 -*-

from datetime import date, datetime
from re import match

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api , exceptions
from odoo.exceptions import ValidationError
import dateutil


class student(models.Model):

    _name ='task1.student'
    _inherit = 'res.users'

    name = fields.Char(string='student name' , required=True)
    age = fields.Integer(string='student age',compute="_compute_age" ,store=True )
    SNN = fields.Char(string="Student SNN" )
    email = fields.Char(string="student email")
    dateOfBirth = fields.Date( string="student date of birth" , required=True)
    image=fields.Binary(attachment=True, help="student image" , string="student image")
    class_id = fields.Many2one('task1.classes', string="student class" , required=True)
    User = fields.Many2one('res.user', string="Student user")
    add_user=fields.Many2one('res.user')



    @api.multi
    @api.depends('dateOfBirth')
    def _compute_age(self):
        for record in self:
            if record.dateOfBirth :
                dt = record.dateOfBirth
                d1 = datetime.strptime(dt, "%Y-%m-%d").date()
                d2 = date.today()
                rd = relativedelta(d2, d1)
                record.age= str(rd.years)
    @api.one
    @api.constrains('email')
    def validate_email(self):
        if self.email:
            if match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", self.email) == None:
                raise ValidationError("Please Provide valid Email Address in valid format")
            return True

    # @api.one
    # @api.constrains('SNN')
    # def _validate_SNN(self):
    #     for record in self:
    #         if self.SNN:
    #             if not record.SNN.isnumeric() :
    #                 raise ValidationError("alpha characters is not allowed")
    #             if len(record.SNN) != 14:
    #              raise ValidationError("SNN must be 14 digits")
    #             if not record.SNN.isnumeric() and len(record.SNN) != 14:
    #                 raise ValidationError("SNN must be 14 digits and no characters")
    #
    #             return True


class classes(models.Model):
    _name ="task1.classes"
    name=fields.Char(string="Class Code")
    student_id=fields.One2many("task1.student" ,'class_id', string="my students")




class res_users(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):

        res = super(res_users, self).create(vals)

        res.create({
            'name': self.name, 'email': self.email
        })
        return res

class createStudentUser(models.Model):
    _inherit = 'res.users'
    student_id = fields.One2many("task1.student", 'class_id', string="my students")























