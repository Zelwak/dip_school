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


#----------------------------------------------------------
# Classe
#----------------------------------------------------------

class school_classroom(models.Model):
    """Model pour les Classe de school."""
    _name = "school.classroom"
    _description = u"Classe school"
    _order = "name"

    name        = fields.Char(string="Nom", required=True)
    level       = fields.Selection([('seconde', 'Seconde'),
                                    ('premiere', 'Première'),
                                    ('terminal', 'Terminale')], string="Niveau")
    teacher_id  = fields.One2many('res.partner', 'classroom_id', string="Professeur")
    student_ids = fields.One2many('school.student', 'classroom_id', string="Élèves")
    student_num = fields.Integer(string="Nombre d'élèves", compute="_compute_student_num")

    @api.depends('student_ids')
    def _compute_student_num(self):
        for record in self:
            record.student_num = len(record.student_ids)
