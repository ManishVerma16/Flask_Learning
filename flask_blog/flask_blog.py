from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1>Hello Page Testing!</h1>'


@app.route('/about')
def about():
    return '<h1>About Page Testing!</h1>'


if __name__ == '__main__':  # name = main module if script is directly run by python
    app.run(debug=True)