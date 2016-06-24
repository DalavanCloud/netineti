"""Name String class"""

class NameString(object):
    """Respresents string representation of tokens"""

    def __init__(self, token, tokens):
        self.offsets = {}
        self.name_string = self._from_tokens(token, tokens)
        self.raw_name_string = self.name_string
        self.canonical = ''
        self.canonical_list = []
        self.canonical_pos = []

    def adjust(self, canonical_list, pos):
        """Save canonical, adjust name_string according to canonical form"""
        canonical_words = frozenset(['hybrid_char', 'uninomial', 'genus',
                                          'specific_epithet',
                                          'infraspecific_epithet'])
        self.canonical = ' '.join(canonical_list)
        self.canonical_list = canonical_list
        self.canonical_pos = [p for p in pos if p[0] in canonical_words]
        words_num = len(canonical_list)
        if len(self.canonical_pos) > words_num:
            self.name_string = self.name_string[0:self.canonical_pos[words_num][1]]
            return True
        else:
            return False

    def start(self):
        return self.offsets[0]["offset"]

    def end(self, pos):
        tokens_pos = sorted(self.offsets.keys())
        try:
            return self.offsets[pos]["offset"]
        except KeyError as e:
            for k in tokens_pos:
                if k > pos:
                    return  self.offsets[k]["offset"] - k + pos


    def _from_tokens(self, token, tokens):
        count = 0
        offset = self._append_token(token, 0, count)
        for t in tokens:
            count += 1
            offset = self._append_token(t, offset, count)
        return token.verbatim + ' ' + ' '.join([t.verbatim for t in tokens])

    def _append_token(self, token, offset, count):
        end_pos = offset + len(token.verbatim)
        self.offsets[offset] = {"token": count, "position": "start",
                                "offset": token.start}
        self.offsets[end_pos] = {"token": count, "position": "end",
                                 "offset": token.end}
        return end_pos + 1



