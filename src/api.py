from bs4 import BeautifulSoup
from workflow import web

import logging
import json

class PowerThesaurus:

    def __init__(self, api_url, logger=logging):
        self.api_url = api_url
        self.logger = logger

    def parse_term(self, term_data):
        return {
            'term': term_data['term'],
            'topics': [t['topic'] for t in term_data['topics']],
            'rating': int(term_data['rating']),
            'parts': [p['short_name'] for p in term_data['parts']]
        }

    def extract_terms(self, page_text):
        soup = BeautifulSoup(page_text, 'html.parser')
        script = soup.find('script', src='').getText().strip().split('\n')[0]
        data = json.loads(script[script.find('{'):-1])

        if 'list' not in data:
            return []

        return data['list']['pages'][0]['terms']

    def build_search_url(self, word, query_type):
        return '{}/{}/{}'.format(self.api_url, word.replace(' ', '_'), query_type)

    def search(self, word, query_type):
        r = web.get(self.build_search_url(word, query_type))
        self.logger.debug('response : {} {}'.format(r.status_code, r.url))
        r.raise_for_status()
        data = self.extract_terms(r.text)
        return [self.parse_term(t) for t in data]
