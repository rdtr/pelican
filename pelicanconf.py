#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'@_rdtr'
SITENAME = u'Fix Typos'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['blog']

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'
DRAFT_URL        = 'drafts/{slug}.html'
DRAFT_LANG_URL   = 'drafts/{slug}_{lang}.html'

ARTICLE_URL     = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

DATE_FORMATS = {'en': '%a, %d %b %Y'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Plugin
PLUGINS = ['pelican_gist']

GIST_CACHE_ENABLED = True

# Blogroll
LINKS = (('Github', 'https://github.com/rdtr'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

LINKS = ()

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './themes/my_flex'
