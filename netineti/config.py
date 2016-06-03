"""Reads NetiNeti configuration file"""
# pylint: disable=R0903

import os
import configparser

class Config(object):
    """Reads configuration file and stores data in a dictionary"""
    PATH = os.path.abspath(os.path.dirname(__file__) +
                           "/../config/netineti.cfg")

    def __init__(self):
        cnf = configparser.ConfigParser()
        cnf.read(self.PATH)
        self.config = {s: dict(cnf.items(s)) for s in cnf.sections()}
