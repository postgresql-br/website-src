#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'admin'
SITENAME = 'Comunidade Brasileira de PostgreSQL'
SITEURL = ''
SITELOGO = 'images/logo.png'
SITELOGO_SIZE = '64x64'
FAVICON = 'images/favicon.ico'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt'
LOCALE = 'pt_BR.utf-8'
DATE_FORMATS = {
    'en': '%d/%m/%Y %H:%M',
    'pt': '%d/%m/%Y %H:%M',
}
DEFAULT_DATE_FORMAT = '%d/%m/%Y %H:%M'

THEME = 'themes/pelican-bootstrap3'
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
PLUGIN_PATHS = ['plugins']
#PLUGINS = ['i18n_subsites', 'tag_cloud']
PLUGINS = ['i18n_subsites']
#DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
#DISPLAY_TAGS_ON_SIDEBAR = True
#TAGS_URL = 'tags.html'
HIDE_SIDEBAR = True
BOOTSTRAP_NAVBAR_INVERSE = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Início', '../category/inicio.html'),
    ('Sobre', '../pages/sobre-o-postgresql.html'),
    ('Downloads', '../pages/downloads.html'),
    ('Documentação', '../pages/documentacao.html'),
    ('Eventos', '../category/eventos.html'),
    ('Suporte', '../pages/suporte.html'),
    ('Participe!', '../pages/participe.html'),
)

SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = False
SHOW_DATE_MODIFIED = True
#SIDEBAR_IMAGES = ["images/logo.png"]
CUSTOM_CSS = 'css/custom.css'
STATIC_PATHS = ['images', 'css']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('PostgreSQL.org', 'http://postgresql.org/'),
#         ('PostgreSQL Docs', 'https://www.postgresql.org/docs/'),
#         ('PostgreSQL Wiki', 'https://wiki.postgresql.org'))

# Social widget
#SOCIAL = (('twitter', 'http://twitter.com/postgresqlbr'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
