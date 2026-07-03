"""
Post Forms
----------
This file contains all forms related
to blog posts.
"""

# Import FlaskForm

from flask_wtf import FlaskForm

# Import Form Fields

from wtforms import (
    StringField,
    TextAreaField,
    SubmitField
)

# Import Validators

from wtforms.validators import (
    DataRequired,
    Length
)


# ---------------------------------
# Create / Edit Post Form
# ---------------------------------

class PostForm(FlaskForm):

    # Post Title

    title = StringField(

        "Post Title",

        validators=[

            DataRequired(),

            Length(
                min=5,
                max=200
            )

        ]

    )

    # Post Content

    content = TextAreaField(

        "Post Content",

        validators=[

            DataRequired(),

            Length(
                min=20
            )

        ]

    )

    # Submit Button

    submit = SubmitField(

        "Publish Post"

    )