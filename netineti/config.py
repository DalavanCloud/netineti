"""Reads NetiNeti configuration file"""
import os
import ConfigParser

class Config(object):
    """Reads configuration file and stores data in a dictionary"""
    PATH = os.path.abspath(os.path.dirname(__file__) +
                           "/../config/netineti.cfg")

    def __init__(self):
        cnf = ConfigParser.ConfigParser()
        cnf.read(self.PATH)
        self.config = {s: dict(cnf.items(s)) for s in cnf.sections()}
