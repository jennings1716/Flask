from flask import Flask,render_template,url_for

from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b1cddc006999b3a3307e8e0595ee3954'

posts = [
            {
                "name":"Jennings",
                "age":"40"
            },
            {
                "name":"Janice",
                "age":"50"
            }
        ]   

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html',posts = posts)

@app.route('/about')
def about():
    return render_template('about.html',title ="About")

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html',title="Register", form =form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title="Login", form =form)