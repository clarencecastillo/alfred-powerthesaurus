#!/usr/bin/python
# encoding: utf-8
#
# Copyright © 2019 hello@clarencecastillo.me
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2017-03-06
#

"""
Powerthesaurus API
"""

from workflow import Workflow

import re
import sys
import functools

ICON = 'icon.png'
HELP_URL = 'https://github.com/clarencecastillo/alfred-powerthesaurus'
API_URL = 'https://www.powerthesaurus.org'

# How long to cache results for
CACHE_MAX_AGE = 180  # seconds

def build_cache_key(query, tags):
    """Make filesystem-friendly cache key"""

    key = query + '_' + ';'.join(tags)
    key = key.lower()
    key = re.sub(r'[^a-z0-9-_;\.]', '-', key)
    key = re.sub(r'-+', '-', key)
    return key

def parse_query(raw_input):
    query_type, _, query = raw_input.strip().partition(" ")
    query_type = { 'ant': 'antonyms', 'syn': 'synonyms' }[query_type]
    return query, query_type

def format_term_result(term):
    parts = ' & '.join(term['parts'])
    topics = ' '.join('#{}'.format(t) for t in term['topics'])
    return ' | '.join([str(term['rating']), term['term'], parts, topics])

def build_item_args(term, term_url):

    term_word = term['term']

    return {
        'title': term_word,
        'subtitle': format_term_result(term),
        'autocomplete': term_word,
        'largetext': term_word,
        'copytext': term_word,
        'valid': True,
        'quicklookurl': term_url,
        'icon': ICON,
        'arg': term_url,
        'modifier_subtitles': {
            'cmd': 'Open this term in your browser'
        }
    }

def main(wf):

    wf.logger.debug(wf.args)

    from api import PowerThesaurus

    query, query_type = parse_query(wf.args[0])
    wf.logger.debug('query : {!r} {!r}'.format(query, query_type))

    if not query:
        wf.add_item('Search Powerthesaurus')
        wf.send_feedback()
        return 0

    key = build_cache_key(query, [query_type])
    wf.logger.debug('cache key : {!r} {!r} -> {!r}'.format(query, query_type, key))

    pt = PowerThesaurus(API_URL, wf.logger)

    # Fetch terms from cache or from API
    terms = wf.cached_data(key, functools.partial(pt.search, query, query_type), max_age=CACHE_MAX_AGE)
    wf.logger.debug('count : {} terms for {!r}'.format(len(terms), query))

    # Show results
    if not terms:
        wf.add_item('No ' + query_type + ' found', 'Try a different word...', icon=ICON)

    for term in terms:
        term_url = pt.build_search_url(term['term'], query_type)
        wf.add_item(**build_item_args(term, term_url))

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow(help_url=HELP_URL, libraries=['./lib'])
    sys.exit(wf.run(main))
