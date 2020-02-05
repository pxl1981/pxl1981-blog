#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site settings
SITENAME = '潘晓亮博客'
SITEURL = 'https://pxl1981.github.io'
AUTHOR = '潘晓亮'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'zh_cn'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

PATH = 'content'
STATIC_PATHS = ['assets', 'images', 'assets/images', 'theme/images']
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
OUTPUT_PATH = 'pxl1981.github.io'

DEFAULT_PAGINATION = 10

# Theme settings
THEME = 'themes/elegant'

PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

ARTICLE_SAVE_AS = 'posts/{slug}.html'
ARTICLE_URL = 'posts/{slug}.html'

AUTHOR_SAVE_AS = ''
AUTHORS = {
    '潘晓亮': {
        'blurb': """潘晓亮，江湖人称亮哥，计算机技术爱好者。""",
        'url': 'https://panxiaoliang.github.io',
    }
}

CATEGORY_SAVE_AS = ''
CATEGORIES_URL = 'categories.html'

TAG_SAVE_AS = ''
TAGS_URL = 'tags.html'

ARCHIVES_URL = 'archives.html'

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

# Landing page settings

LANDING_PAGE_ABOUT = {
    'title': 'Pan Xiaoliang Blog',
    'details': """<p>潘晓亮，江湖人称亮哥，计算机技术爱好者。</p>
        <p>
            <ul>
                <li>邮箱：<a href="mailto:pxl@baihesoftware.com">pxl@baihesoftware.com</a></li>
                <li>网站：<a href="https://panxiaoliang.github.io">https://panxiaoliang.github.io</a></li>
                <li>微信公众号：潘晓亮</li>
            </ul>
        </p>"""
}

PROJECTS = [
    {
        'name': 'panxiaoliang-blog', 
        'url': 'https://github.com/panxiaoliang/panxiaoliang-blog',
        'description': 'Source of the Pan Xiaoliang Blog.',
    },
]

SITE_LICENSE = """Pan Xiaoliang Blog is licensed under the <a rel="license" href="https://creativecommons.org/licenses/by/4.0/"> Creative Commons Attribution 4.0 International License</a>.""" 

# Plugin settings
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'neighbors', 'assets']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = 'feeds/all-{lang}.atom.xml'
AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'))

# Social widget
SOCIAL = (('RSS', 'https://panxiaoliang.github.io/feeds/all.atom.xml'),
          ('Email', 'mailto:pxl@baihesoftware.com'))

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
