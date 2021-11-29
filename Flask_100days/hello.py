from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/bye')
def bye():
    return "Bye!"

@app.route('/name/<your_name>')
def greeting(your_name):
    return f'Hello {your_name}!'

if __name__ == "__maim__":
    app.run()


