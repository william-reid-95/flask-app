from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User,Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
    "author":"Bob Fred",
    "title":"Blog Post 1",
    "content":"first post content",
    "date_posted":"April 1, 2020"
    },
    {
    "author":"Jane Doe",
    "title":"Blog Post 2",
    "content":"second post content",
    "date_posted":"July 22, 2022"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts) #render templates must be stored in a folder called 'templates'

@app.route("/about")
def about():
    return render_template('about.html',title="about")

@app.route("/register",methods=["GET","POST"])
def register():
    #clause to prevent logging in  or registering a user while a user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You are now able to login.','success')
        return redirect(url_for('login'))

    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    #clause to prevent logging in or registering a user while a user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)    
            next_page = request.args.get('next') # args is a dict, .get function checks if key exist in dict and retutns None if not, this prevents an error if key not in dict
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            flash("login failed, please check your account information and try again.", "danger")

    return render_template('login.html',title='Login',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html',title='Account')