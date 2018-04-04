#!/usr/bin/python
# encoding: utf-8
#
# Copyright © 2017 hello@clarencecastillo.me
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2017-03-06
#

"""
Powerthesaurus API
"""

from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import re
import sys
import functools

from workflow import Workflow, web

ICON = 'icon.png'
HELP_URL = 'https://github.com/clarencecastillo/alfred-powerthesaurus'
API_URL = 'https://www.classicthesaurus.org/'

# How long to cache results for
CACHE_MAX_AGE = 20  # seconds

# h.unescape() turns HTML escapes back into real characters
h = HTMLParser()

log = None

def cache_key(query, tags):
    """Make filesystem-friendly cache key"""

    key = query + '_' + ';'.join(tags)
    key = key.lower()
    key = re.sub(r'[^a-z0-9-_;\.]', '-', key)
    key = re.sub(r'-+', '-', key)
    log.debug('cache key : {!r} {!r} -> {!r}'.format(query, tags, key))
    return key

def parse_word(word):
    """Extract info from crawling results"""

    parsers = {
        'word' : {
            'tag' : 'a',
            'class' : 'topic-link'
        },
        'rating' : {
            'tag' : 'div',
            'class' : 'rating'
        },
        'tags' : {
            'tag' : 'span',
            'class' : 't',
            # adds ' | ' between kind of word and other related words
            'sanitize' : lambda t: t[::-1].replace('.', ' | .', 1)[::-1]
        }
    }

    result = { }
    for key, parser in parsers.iteritems():
        element = word.find(parser['tag'], parser['class'])
        result[key] = h.unescape(element.getText()) if element else ""
        result[key] = parser['sanitize'](result[key]) if 'sanitize' in parser else result[key]

    return result

def get_words(query, query_type):
    """Extract list of words from query"""

    r = web.get(API_URL + query.replace(" ", "_") + "/" + query_type)
    log.debug('response : [{}] {}'.format(r.status_code, r.url))
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    results = [parse_word(s) for s in soup.find_all('tr', 'theentry')]
    return results

def main(wf):

    query_type, _, query = wf.args[0].strip().partition(" ")
    log.debug('query : {!r} {!r}'.format(query, query_type))

    query_type = {
        'ant': 'antonyms',
        'syn': 'synonyms'
    }[query_type]

    if not query:
        wf.add_item('Search Powerthesaurus')
        wf.send_feedback()
        return 0

    key = cache_key(query, [query_type])

    # Fetch words from API
    words = wf.cached_data(key, functools.partial(get_words, query, query_type),
                               max_age=CACHE_MAX_AGE)
    log.debug('count : {} words for {!r}'.format(len(words), query))

    # Show results
    if not words:
        wf.add_item('No ' + query_type + 's found',
                    'Try a different word...',
                    icon=ICON)

    for word in words:
        wf.add_item(word['word'],
                    word['rating'] + ' | ' + word['tags'],
                    valid=True,
                    largetext=word['word'],
                    copytext=word['word'],
                    icon=ICON,
                    arg=word['word'])

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow(help_url=HELP_URL)
    log = wf.logger
    sys.exit(wf.run(main))
