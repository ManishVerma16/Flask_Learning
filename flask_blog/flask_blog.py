from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')  # setting multiple route for the same page
def home():
    return '<h1>Hello Page Testing!</h1>'


@app.route('/about')
def about():
    return '<h1>About Page Testing!</h1>'


if __name__ == '__main__':  # name = main if script is directly run by python
    app.run(debug=True)
# if we import this module somewhere else then this name will be the name of module.