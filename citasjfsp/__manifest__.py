# -*- coding: utf-8 -*-

{
    'name': "Citas JFSP",

    'summary': """
    Generador de Citas en Odoo con los campos: 
    Cita, Autor de la cita,  
    Fecha de visualización 
    y Orden de visualización
    """,

    "description": """
    Trabajo de SGE 4 de DAM: 
    Creación de módulos para Odoo
    """,

    'author': "José Francisco Sánchez Portillo",
    'website': "https://pacoportillo.es/",

    
    'category': 'Uncategorized',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views_citasjfsp.xml',
    ],
	
	'images': [
        'static/description/icon.png',
    ],
	
	'installable': True,
    'aplication' : True,
    'auto_install': False,  
}
