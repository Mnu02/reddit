import json

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

# db
posts = {
    1: {
      "id": 1,
      "upvotes": 1,
      "title": "My cat is the cutest!",
      "link": "https://i.imgur.com/jseZqNK.jpg",
      "username": "alicia98"
    },
    2: {
      "id": 2,
      "upvotes": 3,
      "title": "Cat loaf",
      "link": "https://i.imgur.com/TJ46wX4.jpg",
      "username": "alicia98"
    }
}

post_id_counter = 3

@app.route("/")
def hello_world():
    return "Hello world!"


# your routes here

# get all posts
@app.route("/api/posts/", methods=["GET"])
def get_all_posts():
    """
    Get all posts from the database
    """
    response = {"posts": list(posts.values())}
    return json.dumps(response), 200

# create a post
@app.route("/api/posts/", methods=["POST"])
def create_post():
    """
    Endpoint to create a post
    """
    global post_id_counter
    body = json.loads(request.data)
    title = body["title"]
    link = body["link"]
    username = body["username"]
    post = {"id": post_id_counter, "upvotes": 0, "title": title, "link": link, "username": username}
    posts[post_id_counter] = post
    post_id_counter += 1
    return json.dumps(post), 201


# get a specific post by id
@app.route("/api/posts/<int:id>/", methods=["GET"])
def get_post_by_id(id):
    """
    Endpoint to get a post by its id
    """
    post = posts.get(id)
    if post is None:
        return json.dumps({"error": "Post not found"}), 404
    return json.dumps(post), 200

# delete a specific post by id

# get comments for a specific post

# post a comment for a specific post

# edit a comment for a specific post


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
