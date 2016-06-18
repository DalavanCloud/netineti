"""Performs separation of names from non-names in name-candidates"""
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
        is_genus = self._is_genus(g, sp)
        species = []
        if is_genus:
            species = self._relaxed_species(sp)
        else:
            species = self._strict_species(sp)
        if species:
            return g + ' ' + ' '.join(species)
        elif is_genus:
            return g
        else:
            return ''

    def _relaxed_species(self, species):
        res = [s for s in species if (features.is_known_species(s) or
                                      features.is_ambiguous_species(s))]
        return res

    def _strict_species(self, species):
        res = [s for s in species if features.is_known_species(s)]
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
        pass
