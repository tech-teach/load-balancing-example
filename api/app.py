import os

from apistar.frameworks.wsgi import WSGIApp as App
from apistar.http import Response, Request
from apistar import Route
from psutil import cpu_percent


class CORSApp(App):
    """
    Wraps an app, so that it injects CORS headers.
    """

    def finalize_response(self, response: Response) -> Response:
        """
        Inject cors headers and finalize.
        """
        response = super().finalize_response(response)
        content, status, headers, content_type = response
        headers['Access-Control-Allow-Origin'] = '*'
        headers['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Authorization'
        headers['Access-Control-Allow-Credentials'] = 'true'
        headers['Access-Control-Allow-Methods'] = 'GET'
        return Response(content, status, headers, content_type)


def greet():
    """
    Greet our user.
    """
    return {
        'message': 'Hi there fella',
        'hostname': os.environ.get('HOSTNAME'),
    }


def cpu():
    return cpu_percent(interval=1, percpu=True)


ROUTES = [
    Route('/', 'GET', greet),
    Route('/cpu', 'GET', cpu),
]


app = CORSApp(routes=ROUTES)
