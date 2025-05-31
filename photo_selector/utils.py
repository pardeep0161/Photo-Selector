from functools import wraps
from flask import make_response, request, current_app

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == current_app.config["USER"] and auth.password == str(current_app.config["PASS"]):
            return f(*args, **kwargs)
        return make_response("<h1>Access Denied</h1>", 401, {'WWW-Authenticate': 'Basic realm="Login required"'})
    
    return decorated
