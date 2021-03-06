from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Lawrence Fung',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Dec 07, 2021'
    },
    {
        'author': 'Lilian Li',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Dec 06, 2021'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)  #the posts vaulable 'posts' here will be passed to the Home page

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)