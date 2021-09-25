import io

import six

from . import syaml


def load(fp):
    create_reader = syaml.SyamlReaderFactory()
    reader = create_reader()
    return reader(fp)


def loads(text, encoding='utf8'):
    if isinstance(text, six.text_type):
        text = text.encode(encoding)

    if isinstance(text, six.binary_type):
        with io.BytesIO(text) as fp:
            fp.seek(0)
            return load(fp)
    else:
        raise ValueError(
            'text must be str or byte strings: type={}, encoding={}'.format(
                type(text), encoding))
