import configparser
import datetime
import getpass
import sys


def bootstrap_config(config):

    config_file = configparser.ConfigParser()
    config_file.read(config['config_file'])

    if not config_file['DEFAULT']:
        print(f'No [DEFAULT] section in config file {config["config_file"]}. Please use correct format. Stopping...')
        sys.exit()

    # Check mandatory values that cannot be defaulted:
    default = config_file['DEFAULT']
    if not default.get('process_name'):
        print_error_and_exit('process_name')

    if not default.get('restart_command'):
        print_error_and_exit('restart_command')

    if not default.get('smtp_server'):
        print_error_and_exit('smtp_server')

    if not default.get('smtp_user'):
        print_error_and_exit('smtp_user')

    if not default.get('alert_recipient'):
        print('Alert recipient not defined, using smtp-user')
        default['alert_recipient'] = default.get('smtp_user')

    if not default.get('smtp_password'):
        default['smtp_password'] = getpass.getpass(
            f'Please enter smtp server password for user {default.get("smtp_user")}: ')

    # Test if log file can be written
    try:
        with open(default.get('log_file'), 'w') as f:
            f.write('starting daemon @' + str(datetime.datetime.now()) + '\n')
            f.close()
            pass
    except IOError as x:
        print('Cannot open logfile. Stopping...')
        sys.exit()

    config.update(default)
    print("Configuration ready")
    print("-------------------")
    for k in config:
        if k != 'smtp_password':
            print('%s: %s' % (k, config[k]))


def print_error_and_exit(key):
    print(f'Config value {key} not set. Please set it in config-file. Stopping...')
    sys.exit()
