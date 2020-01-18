import urllib
import base64
import re


class DataUrl:

    """
    This object does not support parsing dataurls, do not use hidden methods
    """

    def __init__(self, mimetype=None, data=None, encode_to_b64=False):
        self.mimetype = mimetype or 'text/plain'
        self.encode_to_b64 = encode_to_b64
        self.data = data or str()

    @classmethod
    def __from_url(cls, url):
        data_url = cls.__parse_url(url)
        mimetype = data_url['mediatype']
        encode_to_b64 = bool(data_url['base64'])
        data = base64.b64decode(bytes(data_url['data'], 'utf8')).decode('utf8')

        data_url_obj = cls(
            mimetype=mimetype,
            encode_to_b64=encode_to_b64,
            data=data,
            )

        return data_url_obj

    @staticmethod
    def __parse_url(url):
        url_regex = re.compile(
                'data:(?P<mediatype>[a-z-]+/[a-z-]+){0,1}'
                '(?P<base64>;base64){0,1},'
                '(?P<data>[a-zA-Z0-9-._~%:;,/?#\[\]@!$&\'()*+,=]*)'
            )
        match = url_regex.search(url)
        if not match:
            raise TypeError('Invalid data url')
        return match.groupdict()

    def _generate_url(self):
        if self.encode_to_b64:
            data = base64.b64encode(bytes(self.data, 'utf8')).decode('utf8')
            base64_flag = ';base64'
        else:
            base64_flag = ''
            data = urllib.parse.quote(self.data)
        url = 'data:{}{},{}'.format(
            self.mimetype,
            base64_flag,
            data,
            )
        return url

    def to_uri(self):
        return self._generate_url()


def generate_data_uri(mimetype, data, encode_to_b64=False):
    return DataUrl(
            mimetype=mimetype,
            data=data,
            encode_to_b64=encode_to_b64
        ).to_uri()
