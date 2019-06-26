import json

class ReadOnlyModification(Exception):
    pass


class ReadOnlyDict(dict):

    def __setitem__(self, key, value):
        raise ReadOnlyModification(f"{__class__.__name__} doesn't support item assignment after instantiation.")

    def __delitem__(self, key, value):
        raise ReadOnlyModification(f"{__class__.__name__} doesn't support item deletion after instantiation.")


class NonRewritableDict(dict):
    # An item can be deleted and redefined, but not modified while still in existence
    def __setitem__(self, key, value):
        if key in self:
            raise ReadOnlyModification(f"{__class__.__name__} doesn't support item modification.")

        # Not working yet
        return super().__setitem__(key, value)


class JSONDict(dict):

    def __repr__(self):
        return json.dumps(self, indent=4, sort_keys=True, default=str)


class RegexDict(dict):

    def __init__(self, **kwargs):
        self._patterns = {pattern_str: re.compile(pattern_str) for pattern_str in kwargs}
        super().__init__(**kwargs)

    def _get_matching_keys(self, key):
        matching_keys = []
        for pattern_str, regex in self._patterns.items():
            if regex.search(key):
                matching_keys.append(pattern_str)

        return matching_keys

    def _get_and_check_matching_key(self, key):
        matching_keys = self._get_matching_keys(key)

        if len(matching_keys) == 0:
            raise RuntimeError(f"No key regexes match the key '{key}'")
        elif len(matching_keys) > 1:
            raise RuntimeError(f"More than one key regex matches the key '{key}': {matching_keys}")

        return matching_keys[0]

    def __setitem__(self, key, value):
        regex_key = self._get_and_check_matching_key(key)
        return super().__setitem__(regex_key, value)

    def __getitem__(self, key):
        regex_key = self._get_and_check_matching_key(key)
        return super().__getitem__(regex_key)


class RegexCollection:
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

    obj(text) -> obj.match.url
                 obj.match.picture

    """
    pass
