# -*- coding: utf-8 -*-
##############################################################################
#
#    Gestion de lycée
#    Copyright (C) 2018 Gestion de lycée.
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

from odoo import models, fields, api, _
# from odoo.exceptions import Warning
from datetime import datetime
from dateutil.relativedelta import relativedelta


#----------------------------------------------------------
# Elève
#----------------------------------------------------------

class school_student(models.Model):
    """Model pour les Elève de school."""
    _name = "school.student"
    _description = u"Elève school"
    _order = "display_name"
    _rec_name = "display_name"

    display_name    = fields.Char(string="Nom", compute="_compute_display_name")
    firstname       = fields.Char(string="Prénom", required=True)
    lastname        = fields.Char(string="Nom", required=True)
    birthdate       = fields.Date(string="Date de naissance")
    age             = fields.Integer(string="Âge", compute="_compute_age")
    classroom_id    = fields.Many2one('school.classroom', string="Classe")

    @api.depends('birthdate')
    def _compute_age(self):
        current = datetime.now()
        for record in self:
            if record.birthdate:
                record.age = relativedelta(current, datetime.strptime(record.birthdate, "%Y-%m-%d")).years

    @api.depends('firstname','lastname')
    def _compute_display_name(self):
        for record in self:
            firstname = record.firstname or ''
            lastname = record.lastname or ''
            record.display_name = ' '.join((firstname, lastname))