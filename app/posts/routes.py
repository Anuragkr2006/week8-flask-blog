"""
Post Routes
-----------
This file contains all routes related
to blog posts.
"""

# Import Required Modules

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request
)

from flask_login import (
    login_required,
    current_user
)

from app import db

from app.models import Post

from app.posts.forms import PostForm

from app.comments.forms import CommentForm

# Create Blueprint

posts = Blueprint(
    "posts",
    __name__,
    url_prefix="/posts"
)


# ---------------------------------
# All Posts
# ---------------------------------

@posts.route("/")
def all_posts():

    posts = Post.query.order_by(
        Post.created_at.desc()
    ).all()

    return render_template(

        "posts/all_posts.html",

        title="All Posts",

        posts=posts

    )


# ---------------------------------
# Create Post
# ---------------------------------

@posts.route(
    "/create",
    methods=["GET", "POST"]
)
@login_required
def create_post():

    form = PostForm()

    if form.validate_on_submit():

        post = Post(

            title=form.title.data,

            content=form.content.data,

            user_id=current_user.id

        )

        db.session.add(post)

        db.session.commit()

        flash(

            "Post created successfully.",

            "success"

        )

        return redirect(

            url_for("posts.all_posts")

        )

    return render_template(

        "posts/create_post.html",

        title="Create Post",

        form=form

    )
# ---------------------------------
# Post Details
# ---------------------------------


@posts.route(
        "/<int:post_id>",
        methods=["GET"]
)
       

def post_details(post_id):

    post = Post.query.get_or_404(
        post_id
    )

    comment_form = CommentForm()

    return render_template(

        "posts/post_details.html",

        title=post.title,

        post=post,

        form=comment_form

    )
# ---------------------------------
# My Posts
# ---------------------------------

@posts.route("/my-posts")
@login_required
def my_posts():

    posts = Post.query.filter_by(

        user_id=current_user.id

    ).order_by(

        Post.created_at.desc()

    ).all()

    return render_template(

        "posts/all_posts.html",

        title="My Posts",

        posts=posts

    )
# ---------------------------------
# Edit Post
# ---------------------------------

@posts.route(
    "/edit/<int:post_id>",
    methods=["GET", "POST"]
)
@login_required
def edit_post(post_id):

    post = Post.query.get_or_404(
        post_id
    )

    # Only Owner Can Edit

    if post.user_id != current_user.id:

        flash(

            "You cannot edit this post.",

            "danger"

        )

        return redirect(

            url_for("posts.all_posts")

        )

    form = PostForm()

    if form.validate_on_submit():

        post.title = form.title.data

        post.content = form.content.data

        db.session.commit()

        flash(

            "Post updated successfully.",

            "success"

        )

        return redirect(

            url_for(

                "posts.post_details",

                post_id=post.id

            )

        )

    if request.method == "GET":

        form.title.data = post.title

        form.content.data = post.content

    return render_template(

        "posts/edit_post.html",

        title="Edit Post",

        form=form

    )


# ---------------------------------
# Delete Post
# ---------------------------------

@posts.route(
    "/delete/<int:post_id>"
)
@login_required
def delete_post(post_id):

    post = Post.query.get_or_404(
        post_id
    )

    # Only Owner Can Delete

    if post.user_id != current_user.id:

        flash(

            "You cannot delete this post.",

            "danger"

        )

        return redirect(

            url_for("posts.all_posts")

        )

    db.session.delete(post)

    db.session.commit()

    flash(

        "Post deleted successfully.",

        "success"

    )

    return redirect(

        url_for("posts.all_posts")

    )