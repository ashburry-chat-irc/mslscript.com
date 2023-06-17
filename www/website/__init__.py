#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import annotations

from flask import session, redirect, flash
from shutil import copytree
from configparser import ConfigParser
from os import path, mkdir
users: ConfigParser[str, str] = ConfigParser()

def load_users_ini(username: str):
    username = username.strip()
    username_low: str = username.lower()
    users.read(path.expanduser("~/website_and_proxy/users/") + f"{username_low}/{username_low}.ini")
    return users


def load_default_user():
    users.read(path.expanduser("~/website_and_proxy/default_user.ini")
    return users


def login_user_post(username, password):
    try:
        session['logged_in'] = 'False'
        username_low: str = username.lower()
        load_users_ini(username)
        if users['password'] == password:
            session['logged_in'] = 'True'
            session['username'] = users['home']['username']
            save_user()
            return render_template('/irc/proxies.html')
        else:
            flash('Bad password!', category='error')
            return redirect('/login.html')
    except (ValueError, KeyError):
        flash("Unknown UserName.", category="error")
        return redirect("/login.html")

def register_user_post(username: str, pass1: str, pass2: str):
    password1: str = pass1.strip()
    password2: str = pass2.strip()
    username: str = username.strip()
    username_low: str = username.lower()
    session.clear()
    session['username'] = username
    session['logged_in'] = 'False'
    users.clear()
    try:
        users.read(path.expanduser("~/website_and_proxy/users/") + f"{username}/{username_low}.ini")
        if users['home']['password'] == pass1 or users['home']['password'] == pass2:
            session['logged_in'] = True
            session['username'] = users['home']['username']
    except (KeyError, ValueError):
        if not username:
            flash("Missing UserName in form.", category='error')
        if '.' in username or ':' in username:
            flash("The period or dot (.) the full-colon (:) and the at-sign (@) are not in UserName. They are reserved.", category="error")
            return redirect('/register.html')
        if users.has_section(username):
            flash('UserName already exists.', category='error')
        elif 'admin' in username:
            flash("UserName MUST NOT contain the word 'Admin'", category='error')
        elif username  == 'username':
            flash("Bad choice of UserName", category='error')
        elif len(username) < 3 or len(username) > 10:
            flash("UserName cannot be more than 10 nor less-than 3 characters.", category="error")
            return redirect('/register.html')
        elif len(password1) < 5:
            flash('Password must be at least 5 characters.', category='error')
        elif len(password1) > 15:
            flash('Password must be, at most, 15 characters.', category='error')
        elif not password1 or not password2:
            flash("You missed one of the password entry fields.", category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        else:
            try:
                session["username"] = username
                session["password"] = password1
                session['logged_in'] = 'True'
                src_dir = path.join(path.expanduser("~"), "website_and_proxy", "default_user")
                dest_dir = path.join(path.expanduser("~"), "website_and_proxy", "users", f"{username_low}")
                copytree(src_dir, dest_dir)
                mkdir()
                save_user()
                return redirect('/irc/proxies.html')
            except (FileExistsError, AttributeError, FileNotFoundError):
                save_user()
                return redirect('/irc/proxies.html')
        return redirect('/register.html')
    save_user()
    return redirect('/irc/proxies.html')

def save_user():
    try:
        username = session['username']
        username_low: str = username.lower()
        if 'home' not in users:
            load_default_user()
        for opt, val in session.items():
            opt = opt.strip()
            val = val.strip()
            if opt and val:
                opt = opt.lower()
                users['home'][opt] = val
        with open(path.expanduser("~/website_and_proxy/users/") + f"{username_low}/{username_low}.ini", 'w') as fp:
            users.write(fp, space_around_delimiters=True)
    except (KeyError, ValueError, FileNotFoundError):
        session.clear()
        users.clear()
        return
    logged = session['logged_in']
    session.clear()
    session['logged_in'] = logged
    if logged == 'True':
        session['username'] = username

_dir = path.dirname(path.abspath(__file__))
app_dir = path.join(_dir, '../app')

