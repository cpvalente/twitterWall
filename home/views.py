from flask import Blueprint, render_template
import os
import csv
import json
from file_read_backwards import FileReadBackwards

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


@web_app.route('/tablecontent.json')
def table_content():
    """Function returns json from csv table."""
    csvfile = open(db_path, 'r')
    fieldnames = ('id', 'date', 'user', 'text', 'status')
    reader = csv.DictReader(csvfile, fieldnames)
    out = json.dumps([row for row in reader])
    return out


@web_app.route('/screen1')
def display_screen1():
    """Function renders tweet screen."""
    return render_template('screen1.html')


@web_app.route('/screen2')
def display_screen2():
    """Function renders tweet screen."""
    return render_template('screen2.html')


@web_app.route('/screencontent.json')
def screen_content():
    """Function returns json from selected data in csv table."""
    limit = 16
    approval_string = 'FOR_REVIEW'
    row_list = []
    with open(db_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        it = 0
        for row in reader:
            if it >= limit:
                break
            elif row['status'] == approval_string:
                row_list.append(row)
                it = it + 1
    out = json.dumps(row_list)
    return out


@web_app.errorhandler(404)  # Not found
@web_app.errorhandler(403)  # Forbidden
@web_app.errorhandler(410)  # Gone
@web_app.errorhandler(500)  # Internal Server Error
def page_not_found(e):
    """Function for error handling."""
    return 'Error encountered {}'.format(e)

if __name__ == '__main__':
    screen_content()
