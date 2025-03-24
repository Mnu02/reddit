import json

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

# db
posts = {
    1: {
      "id": 0,
      "upvotes": 1,
      "title": "My cat is the cutest!",
      "link": "https://i.imgur.com/jseZqNK.jpg",
      "username": "alicia98"
    },
    2: {
      "id": 1,
      "upvotes": 3,
      "title": "Cat loaf",
      "link": "https://i.imgur.com/TJ46wX4.jpg",
      "username": "alicia98"
    },
    3: {}
}

@app.route("/")
def hello_world():
    return "Hello world!"


# your routes here

# get all posts
@app.route("/api/posts/")
def get_all_posts():
    """
    Get all posts from the database
    """
    response = {"posts": list(posts.values())}
    return json.dumps(response)

# create a post

# get a specific post by id

# delete a specific post by id

# get comments for a specific post

# post a comment for a specific post

# edit a comment for a specific post


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
