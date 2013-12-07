#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hristo Deshev'
SITENAME = u'Hristo Deshev'
SITEURL = 'http://deshev.com'
FEED_DOMAIN = SITEURL

TIMEZONE = 'Europe/Sofia'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED = FEED_ATOM  #mnmlist theme uses deprecated FEED config
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

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'github']

EXTRA_PATH_METADATA = {
    'github/CNAME': {'path': 'CNAME'},
}

THEME = 'pelican-themes/mnmlist'
