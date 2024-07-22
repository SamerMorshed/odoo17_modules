{
    'name': 'ToDo Application',
    'version': '1.0',
    'summary': 'Simple ToDo Application',
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'views/todo_templates.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            'todo_app/static/src/xml/todo_app.xml',
        ],
        'web.assets_backend': [
            'todo_app/static/src/js/todo_app.js',
        ],
    },
    'application': True,
    'icon': 'static/description/icon.png',
}