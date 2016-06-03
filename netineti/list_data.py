"""Handles white, black and grey lists of data"""
# pylint: disable=R0903,W0231

import os

DATA_PATH = os.path.dirname(os.path.realpath(__file__)) + "/data/"

class Data(object):
    """An abstract class for data lists"""
    # pylint: disable=E1101

    def __init__(self):
        lst = open(self.PATH)
        self.data = frozenset([l.rstrip() for l in lst])

    def contains(self, word):
        """Checks if a word exists in the list"""
        return word in self.data

    # pylint: enable=E1101

class CommonWords(Data):
    """Dictionary words from English plus most used 1000 words from
    each of these languages: Italian, Portuguese, French and German"""
    PATH = DATA_PATH + "black/common_eu_words.txt"

class BlackBayes(Data):
    """Prepares black list for Naive Bayes"""
    PATH = DATA_PATH + "black/bayes.txt"

class WhiteSpecies(Data):
    """Prepares white list of known species epithets"""
    PATH = DATA_PATH + "white/species.txt"

class WhiteGenera(Data):
    """Prepares white list of known genera"""
    PATH = DATA_PATH + "white/genera.txt"

class WhiteUninomials(Data):
    """Prepares white list of known uninomials"""
    PATH = DATA_PATH + "white/uninomials.txt"

class GreySpecies(Data):
    """Prepares grey list of species which are also normal words
    in European languages (especially English)"""
    PATH = DATA_PATH + "grey/species.txt"

class GreyGenera(object):
    """Prepares grey list of species which are also normal words
    in European languages (especially English)"""
    PATH = DATA_PATH + "grey/genera.txt"

    def __init__(self):
        self.data = {}
        words = [l.rstrip().split(" ") for l in open(self.PATH)]
        for ww in words:
            for w in ww[1:]:
                if ww[0] in self.data:
                    self.data[ww[0]].add(w)
                else:
                    self.data[ww[0]] = set([w])

    def contains(self, word):
        """Checks if a word exists in the grey species list"""
        return word in self.data

    def contains_species(self, genus, species):
        """Checks if a species in known for the genus"""
        return genus in self.data and species in self.data[genus]

class ListData(object):
    """Handles collection of white, grey and black lists"""
    def __init__(self):
        self.black = BlackBayes()
        self.common = CommonWords()
        self.species = WhiteSpecies()
        self.genera = WhiteGenera()
        self.uninomials = WhiteUninomials()
        self.grey_species = GreySpecies()
        self.grey_genera = GreyGenera()
