from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(200), nullable=False)


@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(title=data['title'], content=data['content'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created", "post": {"title": new_post.title, "content": new_post.content}}), 201


@app.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify({"title": post.title, "content": post.content})


@app.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    data = request.get_json()
    post = Post.query.get_or_404(id)
    post.title = data['title']
    post.content = data['content']
    db.session.commit()
    return jsonify({"message": "Post updated", "post": {"title": post.title, "content": post.content}})


@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted"})


if __name__ == '__main__':
    app.run(debug=True)


def prisijungti(vartotojas):
    return vartotojas == 'admin'

def veiksmas(atlikti_veiksma):
    return f'Atliktas veiksmas:{atlikti_veiksma}'

def atsijungti(vartotojas):
    return f'{vartotojas} atsijunge'