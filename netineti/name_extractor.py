"""Performs separation of names from non-names in name-candidates"""
#pylint: disable=R0201
import netineti.features as features

class NameExtractor(object):
    """Takes parsed data, and determines if it contains a name or not"""

    def __init__(self, parsed_data, with_nlp=True):
        self._parsed_data = parsed_data

        canonical = parsed_data["canonical_name"]["value"].split(" ")
        self._extractor = self._extractor_factory(canonical, with_nlp)

    def name_string(self):
        """Extracts a name string out of parsed data"""
        return self._extractor.name_string()

    def _extractor_factory(self, canonical, with_nlp):
        if "×" in canonical:
            return HybridExtractor(canonical, with_nlp)
        elif len(canonical) == 1:
            return UninomialExtractor(canonical, with_nlp)
        else:
            return Extractor(canonical, with_nlp)

class Extractor(object):
    """Extract name-strings from potential species and infraspecies"""
    def __init__(self, canonical, with_nlp):
        self.canonical = canonical
        self.with_nlp = with_nlp

    def name_string(self):
        """Extracts name-string from canonical"""
        g = self.canonical[0]
        sp = self.canonical[1:]
        return self._name_string(g, sp)

    def _name_string(self, gen, spa):
        is_genus = self._is_genus(gen, spa)
        species = []
        if is_genus:
            species = self._relaxed_species(spa)
        else:
            species = self._strict_species(spa)
        if species:
            return gen + ' ' + ' '.join(species)
        elif is_genus:
            return gen
        else:
            return ''

    def _relaxed_species(self, species):
        res = []
        for s in species:
            if (features.is_known_species(s) or
                    features.is_ambiguous_species(s)):
                res.append(s)
            else:
                break
        return res

    def _strict_species(self, species):
        res = []
        for s in species:
            if features.is_known_species(s):
                res.append(s)
            else:
                break
        return res

    def _is_genus(self, genus, species):
        return (features.is_known_genus(genus) or
                features.is_species_ambiguous_genus(genus, species))

class UninomialExtractor(Extractor):
    """Extract name-strings from potential uninomials"""

    def name_string(self):
        """Extracts name-string from canonical"""
        w = self.canonical[0]
        if features.is_known_uninomial(w) or features.is_known_genus(w):
            return w
        else: return ""

class HybridExtractor(Extractor):
    """Extract names from potential hybrids"""

    def name_string(self):
        """Extracts name-string from canonical"""
        elements = [e.strip() for e in ' '.join(self.canonical).split('×')]
        left = [w for w in elements[0].split(" ") if w]
        right = [w for w in elements[1].split(" ") if w]
        if left == []:
            return self._named_hybrid(right)
        elif len(left) == 1:
            return self._short_hybrid(left[0], right)
        else:
            return self._hybrid_formula(left, right)

    def _named_hybrid(self, right):
        ns = self._name_string(right[0], right[1:])
        return '× ' + ns if ns else ''

    def _short_hybrid(self, genus, species):
        res = self._name_string(genus, species).split(' ')
        return res[0] + ' × ' + ' '.join(res[1:]) if len(res) > 1 else res[0]

    def _hybrid_formula(self, left, right):
        left_name = self._name_string(left[0], left[1:])
        right_name = ''
        if features.is_capitalized(right[0]):
            right_name = self._name_string(right[0], right[1:])
        else:
            is_genus = self._is_genus(left[0], right)
            if is_genus:
                right_name = ' '.join(self._relaxed_species(right))
            else:
                right_name = ' '.join(self._strict_species(right))
        return left_name + ' × ' + right_name if right_name else left_name
