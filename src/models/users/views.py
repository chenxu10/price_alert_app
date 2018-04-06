from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect

from src.models.users.user import User

user_blueprint=Blueprint('users',__name__)

@user_blueprint.route('/login',methods=['GET','POST'])
# GET method give the user some data
# The user gives us some data by the web browser
def login_user():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['hashed']
        if User.is_login_valid(email,password):
            session['email']=email
        # tells the browser to other location
            return redirect(url_for(".user_alerts"))
        # return None
    return render_template("users/login.html") # send the user an error if their login was invalid

@user_blueprint.route('/register')
def register_user():
    pass

@user_blueprint.route('/alerts')
def user_alerts():
    pass

@user_blueprint.route('/logout')
def logout_user():
    pass
# check alerts for a specific user
@user_blueprint.route('check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass