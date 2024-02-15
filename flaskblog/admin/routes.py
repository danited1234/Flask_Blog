from flask import render_template, url_for, flash, redirect, Blueprint
from flask_login import login_user, current_user, login_required
from flaskblog.models import Admin
from flaskblog import bcrypt
from .forms import AdminForm

admin=Blueprint('admin',__name__)
@admin.route('/admin')
@login_required
def return_to_admin():
    if current_user.is_authenticated:
        pass
    else:
        return redirect(url_for('admin'))
@admin.route('/admin/login',methods=['GET','POST'])
def admin():
    form=AdminForm()
    if form.validate_on_submit():
        user=Admin.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login Sucessful",'success')
            pass
            
        else:
            flash("Wrong password or username. Kindly try again",'danger')
    return render_template("admin.html",form=form)