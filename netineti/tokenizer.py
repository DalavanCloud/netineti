"""Creates tokens from text"""

import re
from netineti.token import Token

class Tokenizer(object):
    """Takes a text and returns a list of token objects"""
    RE_WORD_DIV = re.compile(r'(?<=[a-z])\s*-\s*\r?\n\s*')

    @staticmethod
    def _next_word_division(divs):
        try:
            match_obj = next(divs)
            return (match_obj.start(), match_obj.end())
        except StopIteration:
            return (-1, -1)


    def __init__(self, text):
        self._text = text


    def tokenize(self):
        """Parses text into list of Token objects and reverses its order
        so the first token becomes the last one

        """
        tokens = []
        pre_tokens = self._pre_tokens()
        divs = re.finditer(Tokenizer.RE_WORD_DIV, self._text)
        div = Tokenizer._next_word_division(divs)
        was_in_div = False
        for t in pre_tokens:
            in_div = div[0] <= t[0][1] <= div[1]
            if in_div and not was_in_div:
                tokens.append((t[0], re.sub(r'-$', '', t[1])))
                was_in_div = True
            elif in_div and was_in_div:
                pass
            elif not in_div and was_in_div:
                was_in_div = False
                tt = tokens.pop()
                tokens.append(((tt[0][0], t[0][1]), tt[1] + t[1]))
                div = Tokenizer._next_word_division(divs)
            else:
                tokens.append(t)
        return [Token(t[0][0], t[0][1], t[1])
                for t in tokens
                if Token.is_tokenizable(t[1])][::-1]

    def _pre_tokens(self):
        """ Collects data into a list of tuples: (int, int), string)
        where first int is start of token, second is end of token, and
        string is its content"""
        spaces = [[0]]
        for m in re.finditer(r'\s', self._text):
            spaces[-1].append(m.start())
            spaces.append([m.end()])
        spaces[-1].append(len(self._text))
        return zip(spaces, re.split(r'\s', self._text))

