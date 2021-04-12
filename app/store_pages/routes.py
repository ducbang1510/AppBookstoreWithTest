from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, login_required, logout_user
from app import create_app, db, login_manager, models
from app.models import User
from . import store_pages_blueprint


@store_pages_blueprint.route('/')
def index():
    return render_template('store_pages/index.html')