from flask import Blueprint, render_template

web_app = Blueprint('home_view', __name__)


@web_app.route('/') # Route for the page
@web_app.route('/home') # Route for the page
def display_home_page():
    return render_template('main.html')


@web_app.route('/screen1')  # Route for the page
def display_screen1():
    return render_template('screen1.html')


@web_app.route('/screen2')  # Route for the page
def display_screen2():
    return render_template('screen2.html')


# ERROR HANDLING
@web_app.errorhandler(404)  # Not found
@web_app.errorhandler(403)  # Forbidden
@web_app.errorhandler(410)  # Gone
@web_app.errorhandler(500)  # Internal Server Error
def page_not_found(e):
    return 'Error encountered: {}'.format(e)