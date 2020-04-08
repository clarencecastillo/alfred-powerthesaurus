#!/usr/bin/python
# encoding: utf-8
#
# Copyright © 2020 hello@clarencecastillo.me
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2017-03-06
#

"""
Powerthesaurus API
"""

from workflow import Workflow3

import re
import sys
import functools

UPDATE_SETTINGS = {
    'github_slug': 'clarencecastillo/alfred-powerthesaurus'
}

ICON = 'icon.png'
HELP_URL = 'https://github.com/clarencecastillo/alfred-powerthesaurus'
API_URL = 'https://api.powerthesaurus.org'
WEB_URL = 'https://www.powerthesaurus.org'

# How long to cache results for
CACHE_MAX_AGE = 7200  # seconds

def build_cache_key(query, *tags):
    key = query + '_' + ';'.join(tags)
    key = key.lower()
    key = re.sub(r'[^a-z0-9-_;\.]', '-', key)
    key = re.sub(r'-+', '-', key)
    return key

def build_thesaurus_item_subtitle(term):
    pos = ' & '.join(term['parts_of_speech'])
    tags = ' '.join('#{}'.format(t) for t in term['tags'])
    return ' | '.join([str(term['rating']), term['word']] + filter(lambda s : len(s.strip()), [pos, tags]))

def build_thesaurus_item(term, query_type):
    return {
        'title': term['word'],
        'subtitle': build_thesaurus_item_subtitle(term),
        'autocomplete': term['word'],
        'largetext': term['word'],
        'copytext': term['word'],
        'valid': True,
        'quicklookurl': {
            'synonym': term['url_synonyms'],
            'antonym': term['url_antonyms']
        }[query_type],
        'icon': ICON,
        'arg': term['word']
    }

def main(wf):

    from api import PowerThesaurus

    input_text = wf.args[0]
    wf.logger.debug('input: {!r}'.format(input_text))

    query_type, query = input_text.split(' ', 1)

    if not query:
        wf.add_item('Search Powerthesaurus')
        wf.send_feedback()
        return 0

    key = build_cache_key(query, query_type)
    wf.logger.debug('cache key: {!r} -> {!r}'.format(input_text, key))

    pt = PowerThesaurus(API_URL, WEB_URL, logger=wf.logger)

    thesaurus_terms = wf.cached_data(key, max_age=CACHE_MAX_AGE)

    if thesaurus_terms is not None:
        wf.logger.debug('cache: found {} {}s for {!r}'.format(len(thesaurus_terms), query_type, query))

    if thesaurus_terms is None:

        # Search term from cache or from API
        term = pt.search_query_match(query)
        wf.logger.debug('search: found matching term for {!r}'.format(query))

        # Fetch thesaurus terms from cache or from API
        thesaurus_terms = wf.cached_data(key, functools.partial(pt.thesaurus_query, (term or {}).get('id'), query_type), max_age=CACHE_MAX_AGE)
        wf.logger.debug('thesaurus: found {} {}s for {!r}'.format(len(thesaurus_terms), query_type, query))

    # Show results
    items = [build_thesaurus_item(t, query_type) for t in (thesaurus_terms or [])]
    for item in items:
        wf_item = wf.add_item(**item)
        cmd_modifier = wf_item.add_modifier('cmd', 'Open this term in your browser')
        cmd_modifier.setvar('url', item['quicklookurl'])

    if not items:
        wf.add_item('No {}s found for \"{}\"'.format(query_type, query), 'Try searching for another word...', icon=ICON)

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow3(help_url=HELP_URL, libraries=['./lib'], update_settings=UPDATE_SETTINGS)

    if wf.update_available:
        wf.start_update()

    sys.exit(wf.run(main))
