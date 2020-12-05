# coding = utf-8
from flask import Blueprint, render_template, redirect, url_for

chat = Blueprint('chat', __name__)


@chat.route('/')
def index():
    return render_template('chat/chat.html')
