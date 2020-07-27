from flask import jsonify
from . import api
from .exceptions import ValidationError

def forbidden(message):
    response = jsonify({'error':'forbidden','message':message})
    response.status_code = 403
    return response


def unauthorized(message):
    response = jsonify({'error':'unauthorized','message':message})
    response.status_code = 401
    return response

def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response

# This is how an api post with no body is handled.
# This gets called because the ValidationError was raised
@api.errorhandler(ValidationError)
def validation_error(e):
    return(bad_request(e.args[0]))
