"""
Database Models
---------------
This file contains all database models
used in the Flask Blog application.
"""

# Import Required Modules

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from flask_login import UserMixin

from app import db
from app import login_manager


# Load Logged-in User

@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


# User Model

class User(UserMixin, db.Model):

    __tablename__ = "users"

    # Primary Key

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Username

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    # Email

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    # Password

    password = db.Column(
        db.String(255),
        nullable=False
    )

    # User Posts

    posts = db.relationship(
        "Post",
        backref="author",
        lazy=True,
        cascade="all, delete"
    )

    # User Comments

    comments = db.relationship(
        "Comment",
        backref="user",
        lazy=True,
        cascade="all, delete"
    )

    # Hash Password

    def set_password(self, password):

        self.password = generate_password_hash(
            password
        )

    # Verify Password

    def check_password(self, password):

        return check_password_hash(
            self.password,
            password
        )

    # String Representation

    def __repr__(self):

        return f"<User {self.username}>"


# Post Model

class Post(db.Model):

    __tablename__ = "posts"

    # Primary Key

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Title

    title = db.Column(
        db.String(200),
        nullable=False
    )

    # Content

    content = db.Column(
        db.Text,
        nullable=False
    )

    # Created Date

    created_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp()
    )

    # Author

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    # Comments

    comments = db.relationship(
        "Comment",
        backref="post",
        lazy=True,
        cascade="all, delete-orphan",
        order_by="Comment.created_at.desc()"
    )

    # String Representation

    def __repr__(self):

        return f"<Post {self.title}>"


# Comment Model

class Comment(db.Model):

    __tablename__ = "comments"

    # Primary Key

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Comment

    comment = db.Column(
        db.Text,
        nullable=False
    )

    # Created Date

    created_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp()
    )

    # User ID

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    # Post ID

    post_id = db.Column(
        db.Integer,
        db.ForeignKey("posts.id"),
        nullable=False
    )

    # String Representation

    def __repr__(self):

        return f"<Comment {self.id}>"