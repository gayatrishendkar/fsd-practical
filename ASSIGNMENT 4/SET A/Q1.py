from flask import Flask 
app = Flask(__name__)
@app.route("/")
def home():
    return "Welcome to home page"
@app.route('/about')
def about():
    return "Welcome to about page"
if __name__== "__main__":
    app.run(debug=True)