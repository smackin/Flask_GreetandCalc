from Flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome_page():
    """Displays Welcome Page message"""
    return "Welcome to the Welcome Page."


@app.route('/welcome/home')
def home_page():
    """Displays Home Page"""
    return " Welcome to the Home Page."

@app.route('/welcome/back')
def welcome_back_page():
    """Page Welcomes returning users"""
    return "Welcome back!  We've Missed you! "
    


   