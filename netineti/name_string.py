"""Name String class"""

class NameString(object):
    """Respresents string representation of tokens"""

    def __init__(self, token, tokens):
        self.offsets = []
        self.name_string = self._from_tokens(token, tokens)
        self.raw_name_string = self.name_string
        self.canonical = ''
        self.canonical_words = frozenset(['hybrid_char', 'uninomial', 'genus',
                                          'species_epithet',
                                          'infraspecific_epithet'])

    def adjust(self, canonical, pos):
        """Save canonical, adjust name_string according to canonical form"""
        self.canonical = ' '.join(canonical)
        canonical_pos = [p for p in pos if p[0] in self.canonical_words]
        words_num = len(canonical)
        if len(canonical_pos) > words_num:
            self.name_string = self.name_string[0:canonical_pos[words_num][1]]
            return True
        else:
            return False


    def _from_tokens(self, token, tokens):
        count = 0
        offset = self._append_token(token, 0, count)
        for t in tokens:
            count += 1
            offset = self._append_token(t, offset, count)
        return token.verbatim + ' ' + ' '.join([t.verbatim for t in tokens])

    def _append_token(self, token, offset, count):
        end_pos = offset + len(token.verbatim)
        self.offsets.append({offset: {"token": count, "position": "start",
                                      "offset": token.start}})
        self.offsets.append({end_pos: {"token": count, "position": "end",
                                       "offset": token.end}})
        return end_pos + 1



