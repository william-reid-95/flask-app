from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User,Post

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))

    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == "password":
            flash('Successfully logged in!', "success")
            return redirect(url_for('home'))
        else:
            flash("login failed, please check your account information and try again.", "danger")

    return render_template('login.html',title='Login',form=form)
