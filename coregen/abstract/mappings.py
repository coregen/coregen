"""
TODO: Module docstirng
"""

import json


class JSONDict(dict):

    def __repr__(self):
        return json.dumps(self, indent=4, sort_keys=True, default=str)


class ReadOnlyDict(dict):
    """
    This class provides a "read only" dictionary.
    dictionary/list values contained in internal dict should be unchangebale.
    Will not use deep copy to provide immutability
    All objects inside will be contained by a class that has all methods
    that may change the dict overrided.
    """


class IndexedDictionary:
    """
    Will provide a indexable object that returns dictionaries
    """


class ListMapping:
    """
    This class will provide a mapping of keys to lists and allows __getitem__
    to be used to get both a list, of a cross section of corresponding index
    of all contained lists
    """


class RegexMapping:
    """
    This class is ment to be used as a collection of regular expressions.
    instantiaion - list or *args - will accept a list of regex strings.

    obj = Object([r'asd', r'dsa'])
    y = obj['asd']
    print y
    asd

    Time value -> instantiation

    Object(regex)(text) -> matches
    Object(regex)(text) -> obj.match.key -> value
    instance.process_stream(text)

    obj(text) -> obj.match.url
                 obj.match.picture

    """
