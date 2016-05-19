"""Creates tokens from text"""

import re
from netineti.iterator import Iterator
from netineti.token import Token

class Tokenizer(object):
    """Takes a text and returns a list of token objects"""
    RE_WORD_DIV = re.compile(r'(?<=[a-z])\s*-\s*\r?\n\s*')

    def __init__(self, text):
        self._text = text
        self._divs = self._end_of_line_divs()
        self._tokens_raw = self._tokens_with_divs()
        self._tokens = []

    def tokenize(self):
        """Parses text into list of Token objects"""
        divs_chunks = re.split(self._text, RE_WORD_DIV)
        space_chunks = re.split(r'\s')

    def _end_of_line_divs(self)
        chunks = re.split(Tokenizer.RE_WORD_DIV, self._text)
        div_chunks = chunks.shift
        divs = {( for d in re.finditer(Tokenizer.RE_WORD_DIV, self._text))
        divs_chunks =
        self._spaces = Iterator(re.finditer(r'\s', text))
