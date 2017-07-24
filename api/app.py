import os

from apistar import App, Route


def greet():
    return {
        'message': 'Hi there fella',
        'hostname': os.environ.get('HOSTNAME'),
    }


ROUTES = [
    Route('/', 'GET', greet),
]


app = App(routes=ROUTES)
