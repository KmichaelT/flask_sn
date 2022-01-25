from flask import abort, render_template,url_for,flash, redirect,request,Blueprint
from flask_login import current_user,login_required
from twittest import db
from twittest.models import Feed
from twittest.feed.forms import FeedsForm

posts = Blueprint('posts',__name__)

# CREATE
@posts.route('/create',methods=['GET','POST'])
@login_required
def create_post():
    form =FeedsForm()

    if form.validate_on_submit():

        post =Feed(title=form.title.data,
                            text=form.text.data,
                            user_id=current_user.id
                            )
        db.session.add(post)
        db.session.commit()
        flash('Blog Post Created')
        return redirect(url_for('core.index'))

    return render_template('create_post.html',form=form)

@posts.route('/',methods=['GET','POST'])
def post():
    posts=Feed.query.all()
    return render_template('index.html', post=posts)



