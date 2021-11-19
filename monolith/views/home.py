from flask import Blueprint, render_template
from werkzeug.utils import redirect
from monolith.auth import current_user
from monolith.database import Message, db


home = Blueprint('home', __name__)

@home.route('/')
def index():
    if current_user is not None and hasattr(current_user, 'id'):
        # calculate the number of notifications 
        # number of message received to read + number of message sent that have been read       

        # get the list of messages that has to be read
        messages = db.session.query(Message).filter(Message.receiver == current_user.id).all()
        return render_template("index.html", number = len(messages))
    else:
        return redirect("/login")
