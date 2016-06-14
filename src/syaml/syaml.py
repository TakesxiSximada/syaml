import io
import os
import functools

import six
import yaml
from mako.template import Template
from zope.interface import implementer

from .interfaces import (
    IParser,
    IPostProcess,
    IPreProcess,
    IReader,
    )


@implementer(IPreProcess)
class SyamlPreProcess(object):
    def __call__(self, fileobj):
        if isinstance(fileobj, six.text_type):
            filepath = fileobj
            tmpl = Template(filename=filepath)
        else:  # may be file like object
            filepath = fileobj.name
            tmpl = Template(fileobj.read())

        abs_file_path = os.path.abspath(filepath)
        kwds = dict(os.environ)
        kwds['here'] = os.path.dirname(abs_file_path)
        kwds['name'] = os.path.basename(abs_file_path)
        kwds['path'] = abs_file_path
        fp = io.BytesIO(tmpl.render(**kwds))
        fp.seek(0)
        return fp


@implementer(IParser)
class SyamlParser(object):
    def __call__(self, fileobj):
        return yaml.load(fileobj.read())


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

read = SyamlReader(
    pre=SyamlPreProcess(),
    parse=SyamlParser(),
    post=SyamlPostProcess(),
    )
