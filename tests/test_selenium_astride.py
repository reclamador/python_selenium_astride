#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_selenium_astride
----------------------------------

Tests for `selenium_astride` module.
"""


from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask.ext.testing import LiveServerTestCase
from selenium import webdriver
import unittest
from tests import pages


class Entry(object):
    def __init__(self, title, text):
        self.title = title
        self.text = text

entries = [Entry('Post1', 'Hello world')]

class SeleniumAstrideTest(LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)

        @app.route('/')
        def show_entries():
            return render_template('show_entries.html', entries=entries)

        @app.route('/add', methods=['POST'])
        def add_entry():
            entries.append(Entry(request.form['title'], request.form['text']))
            return redirect(url_for('show_entries'))

        @app.route('/login', methods=['GET', 'POST'])
        def login():
            error = None
            if request.method == 'POST':
                if request.form['username'] != app.config['USERNAME']:
                    error = 'Invalid username'
                elif request.form['password'] != app.config['PASSWORD']:
                    error = 'Invalid password'
                else:
                    session['logged_in'] = True
                    flash('You were logged in')
                    return redirect(url_for('show_entries'))
            return render_template('login.html', error=error)

        @app.route('/logout')
        def logout():
            session.pop('logged_in', None)
            flash('You were logged out')
            return redirect(url_for('show_entries'))

        app.config['USERNAME'] = 'floren'
        app.config['PASSWORD'] = 'astride'
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        return app

    def setUp(self):
        self.app = self.create_app()
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_check_element(self):
        self.browser.get(self.get_server_url())
        home_page = pages.HomePage(self.browser)
        first_entry_title = home_page.first_entry()
        self.assertEqual('Post1', first_entry_title)

    def test_click_link(self):
        self.browser.get((self.get_server_url()))
        home_page = pages.HomePage(self.browser)
        home_page.go_login()
        login_page = pages.LoginPage(self.browser)
        self.assertEqual('Login', login_page.title_page())

    def test_page_elements(self):
        self.browser.get(self.get_server_url() + '/login')
        login_page = pages.LoginPage(self.browser)
        login_page.username = "floren"
        login_page.username.clear()
        login_page.username = "floren"
        login_page.password = "astride"
        login_page.password.clear()
        login_page.login()
        self.assertIn('Invalid password', login_page.get_error())

if __name__ == '__main__':
    unittest.main()
