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

comments_by_post = {
    1: [  # post_id
        {
            "id": 0,
            "upvotes": 8,
            "text": "Wow, my first Reddit gold!",
            "username": "alicia98"
        },
        {
            "id": 1,
            "upvotes": 3,
            "text": "That's a loaf alright 😸",
            "username": "breadfan91"
        }
    ],
    2: [
        {
            "id": 2,
            "upvotes": 1,
            "text": "Your cat is a model!",
            "username": "catlover22"
        }
    ]
}

post_id_counter = 3
comment_id_counter = 4

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
@app.route("/api/posts/<int:id>/", methods=["DELETE"])
def delete_post_by_id(id):
    """
    Endpoint to delete post with id `id`
    """
    post = posts.get(id)
    if post is None:
      return json.dumps({"error": "Post not found"}), 404
    del posts[id]
    return json.dumps(post), 200

# get comments for a specific post
@app.route("/api/posts/<int:post_id>/comments/", methods=["GET"])
def get_comments_for_specific_post(post_id):
    """
    Endpoint to get all the comments on post with id `post_id`
    """
    post = posts.get(post_id)
    if post is None:
        return json.dumps({"error": "Post does not exist"}), 404
    # so post does exist. you can either return its comments or just an empty list
    post_comments = comments_by_post.get(post_id, [])
    return jsonify({"comments": post_comments}), 200


# post a comment for a specific post
@app.route("/api/posts/<int:post_id>/comments/", methods=["POST"])
def post_comment_for_specific_post(post_id):
    """
    Endpoint to post a comment on a specific post
    """
    global comment_id_counter
    post = posts.get(post_id)
    if post is None:
        return json.dumps({"error": "Post doesn't exist bro"}), 404
    body = json.loads(request.data)
    text = body["text"]
    username = body["username"]
    comment = {"id": comment_id_counter, "upvotes": 0, "text": text, "username": username}
    comments_by_post[post_id].append(comment)
    comment_id_counter += 1
    return json.dumps(comment), 200
    

# edit a comment for a specific post


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
