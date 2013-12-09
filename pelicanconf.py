#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import absolute_import, division, print_function, unicode_literals

AUTHOR = 'Hristo Deshev'
SITENAME = 'Hristo Deshev'
SITESUBTITLE = 'Fixing the web. One app at a time.'
#SITEURL = 'http://deshev.com'

TIMEZONE = 'Europe/Sofia'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
    #('Pelican', 'http://getpelican.com/'),
    #('Python.org', 'http://python.org/'),
    #('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/hdeshev'),
          ('Twitter', 'https://twitter.com/hdeshev'),)

MAIL_USERNAME = 'hristo'
MAIL_HOST = 'deshev.com'
TWITTER_USERNAME = 'hdeshev'
GITHUB_URL = 'https://github.com/hdeshev'

SECTIONS = [
    ('Home', 'index.html'),
    #('Archive', 'archives.html'),
    ('Tags', 'tags.html'),
    #('Projects', 'pages/projects.html'),
    #('Talks', 'pages/talks.html'),
    #('About', 'pages/about-me.html'),
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'github']

EXTRA_PATH_METADATA = {
    'github/CNAME': {'path': 'CNAME'},
}

#THEME = 'pelican-octopress-theme'
THEME = 'flasky-theme'
