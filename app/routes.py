from flask import Blueprint, render_template, redirect, url_for, flash, request
from sqlalchemy import text
from sqlalchemy import func
from datetime import datetime
from sqlalchemy import func

bp = Blueprint('main', __name__)

#Principal
@bp.route('/')
def home():
    return render_template('base.html')

