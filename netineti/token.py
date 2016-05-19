"""Token object keeps information about a word in text"""

class Token(object):
    """Implements logic associated with tokens"""

    def __init__(self, start, end, chars):
        """Builds Token instance

        Keyword arguments
        start -- index of the first letter
        end -- index of the last letter
        value -- string representation of the word

        """
        self.start = start
        self.end = end
        self.chars = chars
        self.verbatim = ''.join(self.chars)

    def has_letters(self):
        """Checks if token has any letters"""
        return len(self.chars) > 1 and any(c.isalpha(c) for c in self.chars)

