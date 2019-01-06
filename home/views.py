from flask import Blueprint, render_template
import os
import csv
import json
import io
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


@web_app.route('/screen_temp')
def display_screen():
    """Function renders tweet screen."""
    return render_template('screen_temp.html')


@web_app.route('/screencontent.json')
def screen_content():
    """Function returns json from selected data in csv table."""
    fieldnames = ('id', 'date', 'user', 'text', 'status', 'screen_id')
    limit = 16
    approval_string = 'FOR_REVIEW'
    row_list = ''

    with FileReadBackwards(db_path, encoding="utf-8") as csvfile:
        # getting lines by lines starting from the last line up
        for it, line in enumerate(csvfile, 1):
            if (it > limit):
                break
            row_list = row_list + line + "\n"

    reader_list = csv.DictReader(io.StringIO(row_list), fieldnames)
    out = json.dumps([row for row in reader_list])
    print (out)
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
