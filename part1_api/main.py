from flask import Flask, render_template
import requests
from post import Post

blog_url='https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(url=blog_url).json()
blogs = []
for blog in response:
    new_blog = Post(blog['id'], blog['title'], blog['body'], blog['subtitle'])
    blogs.append(new_blog)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blogs = blogs)

@app.route('/blog/<int:num>')
def get_blog(num):
    return render_template("post.html", blog = blogs[num])

if __name__ == "__main__":
    app.run(debug=True)
