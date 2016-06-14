import os
from unittest import TestCase


class SyamlDefaultReadTest(TestCase):
    def _get_target(self):
        from ..syaml import read as func
        return func

    def _call_fut(self, *args, **kwds):
        target = self._get_target()
        return target(*args, **kwds)

    def test_fileobj(self):
        yaml_path = './syaml_test.yaml'

        with open(yaml_path) as fp:
            obj = self._call_fut(fp)

        path = os.path.abspath(yaml_path)
        here = os.path.dirname(path)
        name = os.path.basename(path)

        self.assertEqual(obj[0]['here'], here)
        self.assertEqual(obj[1]['name'], name)
        self.assertEqual(obj[2]['path'], path)
        self.assertEqual(obj[3]['test'], 'OK')

    def test_filepath(self):
        yaml_path = './syaml_test.yaml'
        obj = self._call_fut(yaml_path)

        path = os.path.abspath(yaml_path)
        here = os.path.dirname(path)
        name = os.path.basename(path)

        self.assertEqual(obj[0]['here'], here)
        self.assertEqual(obj[1]['name'], name)
        self.assertEqual(obj[2]['path'], path)
        self.assertEqual(obj[3]['test'], 'OK')
