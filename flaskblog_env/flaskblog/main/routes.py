from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home') 
def home():
    # posts = Post.query.all()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page=page) # mainlying pagination to show only limited post on home page
    return render_template('home.html', posts=posts)  # return the home.html using rendered template object


@main.route('/about')
def about():
    return render_template('about.html', title='About')