from flask import Flask, render_template
import requests

blog_url='https://api.npoint.io/8c31d36d153c7e9f67bb'
response = requests.get(url=blog_url).json()


app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html', blogs = response)

@app.route('/contacts')
def contact_page():
    return render_template('contact.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/blog/<int:num>')
def show_blog(num):
    return render_template('post.html', blog = response[num])

if __name__ == "__main__":
    app.run(debug=True)