# -*- coding: utf-8 -*-
{
    'name': 'Gestion de lycée',
    'version': '0.1',
    'category': '',
    'summary': "Gestion de lycée",
    'description': "Module de gestion de lycée",
    'author': 'Flavien CHÊNE (fchene@team-dsi.fr)',
    'website': '',
    'depends': ['base'],
    'data': [
        'security/school_security.xml',
		'views/classroom_view.xml',
		'views/course_view.xml',
		'views/schedule_view.xml',
		'views/student_view.xml',
		'views/res_partner_view.xml',
        'datas/datas.xml',
        'security/ir.model.access.csv',  # A la fin pour que les modèles soient connus
        'school_menu.xml',  # En dernier pour que les ID d'actions soient connus
    ],
    'installable': True,
}