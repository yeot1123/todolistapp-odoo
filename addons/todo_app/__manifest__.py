# -*- coding: utf-8 -*-
{
    'name': 'Todo App',
    'version': '1.0',
    'summary': 'Todo List Application',     
    'category': 'Productivity',
    'author': 'Thanaboon',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_views.xml',
        'views/menu.xml',
        'data/todo_tags_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}