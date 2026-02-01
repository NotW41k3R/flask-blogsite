from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# New Post Form
class CreatePostForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle',validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

# ENDPOINTS

# Home
@app.route('/')
def get_all_posts():
    all_posts = db.session.execute(db.select(BlogPost)).scalars().all()
    posts = [post for post in all_posts]

    return render_template("index.html", all_posts=posts)

# Show Post
@app.route('/post/<int:post_id>',methods=['POST','GET'])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)

    return render_template("post.html", post=requested_post)

# New Post
@app.route('/new-post', methods=['POST','GET'])
def create_new_post():
    new_post = CreatePostForm()
    if new_post.validate_on_submit():
        new_blog = BlogPost(
            title = new_post.title.data,
            subtitle = new_post.subtitle.data,
            date = date.today().strftime('%B %d, %Y'),
            body = new_post.body.data,
            author = new_post.author.data,
            img_url = new_post.img_url.data
        )
        db.session.add(new_blog)
        db.session.commit()
        return redirect (url_for('get_all_posts'))
    return render_template('make-post.html', form=new_post, call_type = 'new')

# Edit Post
@app.route('/edit-post/<post_id>', methods=['POST','GET'])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_post = CreatePostForm(
            title = post.title,
            subtitle = post.subtitle,
            author = post.author,
            img_url = post.img_url,
            body = post.body,
    )
    if edit_post.validate_on_submit():

        post.title = edit_post.title.data
        post.subtitle = edit_post.subtitle.data
        post.date = date.today().strftime('%B %d, %Y')
        post.body = edit_post.body.data
        post.author = edit_post.author.data
        post.img_url = edit_post.img_url.data

        db.session.commit()
        return redirect (url_for('show_post', post_id = post.id))
    
    return render_template('make-post.html', form=edit_post, call_type = 'edit', post=post)

# Delete Post
@app.route('/delete/<post_id>')
def delete_post(post_id):
    db.session.delete(db.get_or_404(BlogPost, post_id))
    db.session.commit()
    return redirect (url_for('get_all_posts'))

# About
@app.route("/about")
def about():
    return render_template("about.html")

# Contact
@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
