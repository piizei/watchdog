import argparse
import os
import sys


def bootstrap_argparse(config):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='specify config file')
    args = parser.parse_args()
    if args.config:
        if check_file(args.config):
            print(f'Using config-file {args.config}')
            config['config_file'] = args.config
        else:
            print(f'Config file {args.config} not found! Stopping...')
            sys.exit()
    else:
        if check_file(config['config_file']):
            print('Using default config-file watchdog.ini')
        else:
            print('Default config watchdog.ini not found, and no alternative specified. Stopping...')
            sys.exit()


def check_file(file):
    return os.path.isfile(file)
