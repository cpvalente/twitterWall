from flask import Blueprint, render_template
import os
from tablib import Dataset

web_app = Blueprint('home_view', __name__)

# get path for db
db_path = os.path.join("/".join(os.path.dirname(__file__).split("/")[:-1]),'db/tweets.csv')
print(db_path)

@web_app.route('/')
@web_app.route('/home')
def display_home_page():
    """Function renders main page showing server status and user options."""
    return render_template('main.html')


@web_app.route('/table')
def display_table():
    """Function renders placeholder table page."""
    return render_template('table.html')


@web_app.route('/tablecontent.html')
def table_content():
    """Function renders table content."""
    dataset = Dataset().load(open(db_path).read())
    return render_template('content.html', data=dataset.html)


@web_app.route('/screen1')
def display_screen1():
    """Function renders tweet screen."""
    return render_template('screen1.html')


@web_app.route('/screen2')
def display_screen2():
    """Function renders tweet screen."""
    return render_template('screen2.html')


@web_app.errorhandler(404)  # Not found
@web_app.errorhandler(403)  # Forbidden
@web_app.errorhandler(410)  # Gone
@web_app.errorhandler(500)  # Internal Server Error
def page_not_found(e):
    """Function for error handling."""
    return 'Error encountered {}'.format(e)
