import io
import os
import functools

import six
import yaml
from mako.template import Template
from zope.interface import implementer
from zope.component import IFactory

from .interfaces import (
    IParser,
    IPostProcess,
    IPreProcess,
    IReader,
    )


NAME = 'syaml'


@implementer(IPreProcess)
class SyamlPreProcess(object):
    def __call__(self, fileobj):
        if isinstance(fileobj, six.string_types):
            filepath = fileobj
            tmpl = Template(filename=filepath)
        else:  # may be file like object
            # fileobj has not name if it not file object
            filepath = getattr(fileobj, 'name', None)
            tmpl = Template(fileobj.read())

        kwds = dict(os.environ)
        if filepath is not None:  # file like object, but not file object
            abs_file_path = os.path.abspath(filepath)
            kwds['here'] = os.path.dirname(abs_file_path)
            kwds['name'] = os.path.basename(abs_file_path)
            kwds['path'] = abs_file_path
        else:
            kwds['here'] = '""'
            kwds['name'] = '""'
            kwds['path'] = '""'
        buf = tmpl.render(**kwds)
        fp = io.BytesIO(buf.encode())
        fp.seek(0)
        return fp


@implementer(IParser)
class SyamlParser(object):
    def __call__(self, fileobj):
        return yaml.load(fileobj.read(), yaml.SafeLoader)


@implementer(IPostProcess)
class SyamlPostProcess(object):
    def __call__(self, obj):
        return obj


@implementer(IReader)
class SyamlReader(object):
    def __init__(self, pre, parse, post):
        self.pre = pre
        self.parse = parse
        self.post = post

    def __call__(self, fileobj):
        return functools.reduce(
            lambda obj, fun: fun(obj),
            (self.pre, self.parse, self.post),
            fileobj,
            )


@implementer(IFactory)
class SyamlReaderFactory(object):
    def __call__(self):
        return SyamlReader(
            pre=SyamlPreProcess(),
            parse=SyamlParser(),
            post=SyamlPostProcess(),
            )


def includeme(config):
    reg = config.registry
    create_reader = SyamlReaderFactory()
    reader = create_reader()
    reg.registerUtility(reader, IReader, NAME)
