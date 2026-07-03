"""
Comment Routes
--------------
This file contains all routes related
to blog comments.
"""

# Import Required Modules

from flask import (
    Blueprint,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from app import db

from app.models import (
    Post,
    Comment,
    User
)

from app.comments.forms import CommentForm


# Create Blueprint

comments = Blueprint(
    "comments",
    __name__,
    url_prefix="/comments"
)


# ---------------------------------
# Add Comment
# ---------------------------------

@comments.route(
    "/add/<int:post_id>",
    methods=["POST"]
)
@login_required
def add_comment(post_id):

    post = Post.query.get_or_404(
        post_id
    )

    form = CommentForm()

    if form.validate_on_submit():

        comment = Comment(

            comment=form.comment.data,

            user_id=current_user.id,

            post_id=post.id

        )

        db.session.add(comment)

        db.session.commit()

        flash(

            "Comment added successfully.",

            "success"

        )

    return redirect(

        url_for(

            "posts.post_details",

            post_id=post.id

        )

    )


# ---------------------------------
# Delete Comment
# ---------------------------------

@comments.route(
    "/delete/<int:comment_id>"
)
@login_required
def delete_comment(comment_id):

    comment = Comment.query.get_or_404(
        comment_id
    )

    if comment.user_id != current_user.id:

        flash(

            "You cannot delete this comment.",

            "danger"

        )

        return redirect(

            url_for(

                "posts.post_details",

                post_id=comment.post_id

            )

        )

    post_id = comment.post_id

    db.session.delete(comment)

    db.session.commit()

    flash(

        "Comment deleted successfully.",

        "success"

    )

    return redirect(

        url_for(

            "posts.post_details",

            post_id=post_id

        )

    )