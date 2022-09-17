from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

#secret key is important for security, need to research further, but it encrypts cookiesd andotehr data.
app.config['SECRET_KEY'] = '015182c115182aa5cc7d6303919cb86d'

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

if __name__ == '__main__':
    app.run(debug=True)