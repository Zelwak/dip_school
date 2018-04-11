# -*- coding: utf-8 -*-
##############################################################################
#
#    DIP IUT
#    Copyright (C) 2018 DIP IUT.
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
# Professeur
#----------------------------------------------------------

class school_teacher(models.Model):
    """Model pour les Professeur de school."""
    _inherit = "res.partner"

    classroom_id = fields.Many2one('school.classroom', string="Classe")