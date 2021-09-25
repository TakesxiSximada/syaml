import os
import logging

import yaml
from mako.template import Template
from zope.interface import implementer
from zope.component import IFactory

from .volumes import Volume
from .interfaces import ISetting

_logger = logging.getLogger(__name__)


@implementer(ISetting)
class VolumeSetting(dict):
    def __init__(self, *args, **kwds):
        super(VolumeSetting, self).__init__(*args, **kwds)
        self.project_name = None  # docker-compose project
        self.name = None
        self.dry_run = False

    def get_volume_name(self, name):
        if name not in self:
            raise KeyError(name)
        return '{}_{}'.format(self.project_name, name)

    def set_name(self, name):
        self.name = name

    def set_dry_run(self):
        self.dry_run = True


@implementer(IFactory)
class VolumeSettingParser(object):
    def __init__(self, env, path, project_name=''):
        self.env = env
        self.path = path
        self.project_name = project_name

    def __call__(self, env=None, path=None, project_name=None):
        env = self.env if env is None else env
        path = self.path if path is None else path
        project_name = self.project_name \
            if project_name is None else project_name

        kwds = dict(os.environ)
        kwds['here'] = os.path.abspath(os.path.dirname(path))

        tmpl = Template(filename=path)
        data = yaml.load(tmpl.render(**kwds))

        setting = VolumeSetting()
        setting.set_name(env)
        setting.project_name = project_name
        for volume_name, volume_data in data['volumes'].items():
            volume = Volume(**volume_data)
            setting[volume_name] = volume
        return setting
