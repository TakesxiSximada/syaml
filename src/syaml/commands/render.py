import sys
import json
import argparse

import yaml
import syaml.syaml


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('--pre', default=None, action='store_true')
    parser.add_argument('--json', default=None, action='store_true')
    args = parser.parse_args(argv)

    path = args.path

    if args.pre:
        pre = syaml.syaml.SyamlPreProcess()
        with open(path, 'rb') as fp:
            print(pre(fp).read().decode())
    else:
        create_reader = syaml.syaml.SyamlReaderFactory()
        reader = create_reader()
        with open(path, 'rb') as fp:
            obj = reader(fp)
        if args.json:
            buf = json.dumps(obj)
        else:
            buf = yaml.dump(obj, default_style=None, default_flow_style='')
        print(buf)
