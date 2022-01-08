from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/my_browser')
def my_browser():
    user_agent = request.headers.get('User-Agent')
    return f"You are using {user_agent}"

@app.route('/bye')
def bye():
    return "Bye!"

@app.route('/name/<your_name>')
def greeting(your_name):
    return f'Hello {your_name}!'


if __name__ == "__main__":
    app.run(debug=True)


