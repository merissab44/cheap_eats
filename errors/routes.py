"""Handle errors to provide positive user experience."""
from flask import Blueprint, render_template

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(404)
def show404(err):
    """Show 404 page."""
    print(err)
    return render_template("404.html")


@errors.app_errorhandler(500)
def show500(err):
    """Show 500 page."""
    print(err)
    return render_template("500.html")
