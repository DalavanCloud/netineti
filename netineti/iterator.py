"""Modification of python iterator to hide StopIteration exception"""

class Iterator(object):
    """Iterator class returns None instead of raising StopIteration
    exception"""

    def __init__(self, iterator):
        self._iterator = iterator

    def next(self):
        """Returns either next element, or None"""
        try:
            return self._iterator.next()
        except StopIteration:
            return None
