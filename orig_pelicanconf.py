#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"PSF"
SITENAME = u"PSF Outreach & Education"
SITEURL = 'http://psf-outreach.org'
TIMEZONE = 'America/Los_Angeles'

GITHUB_URL = 'http://github.com/econchick/psfoutreach'
DISQUS_SITENAME = 'psfoeblog'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

DEFAULT_LANG = 'en'

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS =  (('PSF', 'http://python.org/psf'),
          ('Python.org', 'http://python.org'),
          ('PSF Blog', 'http://pyfound.blogspot.com'),)

# Social widget
SOCIAL = (('Twitter', 'http://www.twitter.com/ThePSF'),
          ('Facebook', 'http://www.facebook.com/#!/pythonlang'),)

DEFAULT_PAGINATION = 10

PLUGINS = ['pelican.plugins.sitemap']
SITEMAP = {
        'format' : 'xml',
        'priorities': {
            'articles': 0.5,
            'indexes': 0.5,
            'pages': 0.5
        },
        'changefreqs': {
            'articles': 'monthly',
            'indexes': 'daily',
            'pages': 'monthly'
        }
}
SUMMARY_MAX_LENGTH = 100
