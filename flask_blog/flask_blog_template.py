from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Raju Rastogi',
        'title': 'Blog1',
        'content': 'First blog content',
        'date_posted': 'March 24, 2021',
    },
    {
        'author': 'Farhan Quershi',
        'title': 'Blog2',
        'content': 'Second blog content',
        'date_posted': 'March 24, 2021',
    }
]

@app.route('/')
@app.route('/home') 
def home():
    return render_template('home.html', posts=posts)  # return the home.html using rendered template object


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':  
    app.run(debug=True)

