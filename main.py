from flask import Flask, render_template
import requests
from post import Post
import datetime as dt

app = Flask(__name__)

response = requests.get('https://api.npoint.io/4af156202f984d3464c3')
data = response.json()
my_posts = Post(data)
year = dt.datetime.now().year

@app.route('/')
def home():
    return render_template("index.html", all_posts=my_posts.all_posts, currentYear=year)

@app.route('/post/<un_id>')
def post(un_id):
    post_to_send = my_posts.get_post(un_id)
    return render_template("post.html", cur_post=post_to_send, currentYear=year)


if __name__ == "__main__":
    app.run(debug=True)
