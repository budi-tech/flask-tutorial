import functools  # noqa: F401

from flask import (  # noqa: F401
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash  # noqa: F401

from flaskr.db import get_db  # noqa: F401

bp = Blueprint("auth", __name__, url_prefix="/auth")
