"""Token object keeps information about a word in text"""

class Token(object):
    """Implements logic associated with tokens"""

    def __init__(self, start, end, verbatim):
        """Builds Token instance

        Keyword arguments
        start -- index of the first letter
        end -- index of the last letter
        value -- string representation of the word

        """
        self.start = start
        self.end = end
        self.verbatim = verbatim
