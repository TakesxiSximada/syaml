import io
import os
from unittest import TestCase


def get_path(path):
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        path,
        )


class SyamlDefaultReadTest(TestCase):
    def _call_fut(self, *args, **kwds):
        from .. import syaml
        create_reader = syaml.SyamlReaderFactory()
        reader = create_reader()
        return reader(*args, **kwds)

    def test_fileobj(self):
        yaml_path = get_path('./syaml_test.yaml')
        with open(yaml_path, 'rb') as fp:
            obj = self._call_fut(fp)

        path = os.path.abspath(yaml_path)
        here = os.path.dirname(path)
        name = os.path.basename(path)

        self.assertEqual(obj[0]['here'], here)
        self.assertEqual(obj[1]['name'], name)
        self.assertEqual(obj[2]['path'], path)
        self.assertEqual(obj[3]['test'], 'OK')

    def test_bytesio(self):
        yaml_path = get_path('./syaml_test.yaml')
        with open(yaml_path, 'rb') as fp:
            with io.BytesIO(fp.read()) as dp:
                dp.seek(0)
                obj = self._call_fut(dp)

        path = ''
        here = ''
        name = ''

        self.assertEqual(obj[0]['here'], here)
        self.assertEqual(obj[1]['name'], name)
        self.assertEqual(obj[2]['path'], path)
        self.assertEqual(obj[3]['test'], 'OK')

    def test_filepath(self):
        yaml_path = get_path('./syaml_test.yaml')
        obj = self._call_fut(yaml_path)

        path = os.path.abspath(yaml_path)
        here = os.path.dirname(path)
        name = os.path.basename(path)

        self.assertEqual(obj[0]['here'], here)
        self.assertEqual(obj[1]['name'], name)
        self.assertEqual(obj[2]['path'], path)
        self.assertEqual(obj[3]['test'], 'OK')
