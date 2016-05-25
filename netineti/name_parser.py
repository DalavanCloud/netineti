"""Parsers scientific names"""

import socket
import json
from netineti.config import Config

class NameParser(object):
    """Parsers scientific names"""

    def __init__(self):
        cfg = Config().config['gnparser']
        self.host = cfg["host"]
        self.port = int(cfg["port"])
        self.buffer_size = 1024
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """Connects to ``gnparser`` socket"""
        self.socket.connect((self.host, self.port))

    def stop(self):
        """Disconnects from ``gnparser`` socket"""
        self.socket.close()

    def parse(self, name_string):
        """Sends a name-string to parser and gets back parsed result"""
        self.socket.send(name_string)
        return json.loads(self.socket.recv(self.buffer_size))

    def pos(self, name_string):
        """Returns only positions of words in the name-string"""
        res = self.parse(name_string)
        if res["parsed"]:
            return res["positions"]
        else:
            return []
