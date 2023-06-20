#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import annotations

from flask import session, redirect, flash
from shutil import copytree
from configparser import ConfigParser
<<<<<<< HEAD
from os import path, rename
users: ConfigParser[str, str] = ConfigParser()
user_dir: list[str | None] = [None]
user_file: list[str | None] = [None]

def set_paths(username: str):
    username = username.strip()
    username_low: str = username.lower()
    user_dir[0] = path.join(path.expanduser("~"), "website_and_proxy", "users", f"{username_low}")
    user_file[0] = path.join(path.expanduser("~"), "website_and_proxy", "users", f"{username_low}", f"{username_low}.ini")
=======
from os import path, mkdir
users: ConfigParser[str, str] = ConfigParser()
>>>>>>> 551521c307c70d20660e54401494fe0f89d6f04d

def load_users_ini(username: str):
    username = username.strip()
    username_low: str = username.lower()
<<<<<<< HEAD
    set_paths(username_low)
    users.read(user_file[0])
=======
    users.read(path.expanduser("~/website_and_proxy/users/") + f"{username_low}/{username_low}.ini")
>>>>>>> 551521c307c70d20660e54401494fe0f89d6f04d
    return users


def load_default_user():
<<<<<<< HEAD
    users.read(path.expanduser("~/website_and_proxy/default_user/default_user.ini"))
    return users


def login_user_post(username: str, password: str):
    try:
        session['logged_in'] = 'False'
        username_low: str = username.lower()
        load_users_ini(username_low)
        if users['home']['password'] == password:
            session['logged_in'] = 'True'
            session['username'] = users['home']['username']
            save_user()
            return redirect('/irc/proxies.html')
=======
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
>>>>>>> 551521c307c70d20660e54401494fe0f89d6f04d
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
<<<<<<< HEAD
        load_users_ini(username_low)
        if users['home']['password'] == pass1 or users['home']['password'] == pass2:
            session['logged_in'] = 'True'
            session['username'] = users['home']['username']
            save_user()
            return redirect('/irc/proxies.html')
        else:
            flash('UserName is already in-use, try another one...', category='error')
            session.clear()
            session['logged_in'] = 'False'
            return redirect('/register.html')
    except (KeyError, ValueError):
        if not username:
            flash("Missing UserName in form.", category='error')
        if '.' in username or ':' in username or '@' in username:
            flash("The period or dot (.) the full-colon (:) and the at-sign (@) are not in UserName. They are reserved.", category="error")
=======
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
>>>>>>> 551521c307c70d20660e54401494fe0f89d6f04d
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
<<<<<<< HEAD
                src_file = path.join(path.expanduser("~"), "website_and_proxy", "users", f"{username_low}", 'default_user.ini')
                set_paths(username_low)
                copytree(src_dir, user_dir[0])
                rename(src_file, user_file[0])
                load_users_ini(username_low)
                save_user()
                return redirect('/irc/proxies.html')
            except (FileExistsError,):
                load_users_ini(username_low)
                save_user()
                return redirect('/irc/proxies.html')
        session.clear()
        session['logged_in'] = 'False'
        return redirect('/register.html')

=======
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
>>>>>>> 551521c307c70d20660e54401494fe0f89d6f04d

def save_user():
    try:
        username = session['username']
        username_low: str = username.lower()
<<<<<<< HEAD
        set_paths(username_low)
        if 'home' not in users:
            users['home'] = {}
        for opt, val in session.items():
            opt = str(opt)
            val = str(val)
=======
        if 'home' not in users:
            load_default_user()
        for opt, val in session.items():
>>>>>>> 551521c307c70d20660e54401494fe0f89d6f04d
            opt = opt.strip()
            val = val.strip()
            if opt and val:
                opt = opt.lower()
                users['home'][opt] = val
<<<<<<< HEAD
        with open(user_file[0], 'w') as fp:
=======
        with open(path.expanduser("~/website_and_proxy/users/") + f"{username_low}/{username_low}.ini", 'w') as fp:
>>>>>>> 551521c307c70d20660e54401494fe0f89d6f04d
            users.write(fp, space_around_delimiters=True)
    except (KeyError, ValueError, FileNotFoundError):
        session.clear()
        users.clear()
        return
    logged = session['logged_in']
    session.clear()
    session['logged_in'] = logged
    if logged == 'True':
<<<<<<< HEAD
        session['username'] = username_low
=======
        session['username'] = username
>>>>>>> 551521c307c70d20660e54401494fe0f89d6f04d

_dir = path.dirname(path.abspath(__file__))
app_dir = path.join(_dir, '../app')

