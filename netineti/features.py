"""Features for various distinguishing characteristics of scientific names"""
import string
from netineti.token import Token
from netineti.list_data import ListData

LISTS = ListData()

def is_token(obj):
    """Checks if an object is of a Token type"""
    return isinstance(obj, Token)

def is_capitalized(word):
    """Checks if a token starts with a capital character"""
    return len(word) > 1 and word[0] in string.ascii_uppercase + 'ŒÆ'

def is_like_hybrid_sign(word):
    """Checks if a token starts with a hybrid sign"""
    return (len(word) == 1 and word[0] in "xX×" or
            word[0] in "x×" and is_capitalized(word[1:]))

def is_known_uninomial(word):
    """Checks if a word is a known uninomial"""
    return LISTS.in_uninomials(word)

def is_known_genus(word):
    """Checks if a word is a known genus"""
    return LISTS.in_genera(word)

def is_known_species(word):
    """Checks if a word is a known species epithet"""
    return LISTS.in_species(word)
