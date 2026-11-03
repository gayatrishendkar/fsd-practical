from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Name: Gayatri Shendkar<br>Roll Number: 01"
if __name__ == "__main__":
    app.run(debug=True)