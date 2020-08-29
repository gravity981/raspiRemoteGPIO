import json
import sys

def read_config() -> dict:
    # read file
    with open('config.json', 'r') as configFile:
        data = configFile.read()

    # parse file
    config = json.loads(data)
    return config


def check_config(config: dict) -> bool:
    if not 'server' in config:
        return False
    if not 'device' in config:
        return False
    if not 'port' in config['server']:
        return False
    if not type(config['server']['port']) is int:
        return False
    return True


def main():
    config = read_config()
    if not check_config(config):
        print('invalid configuration')
        sys.exit(1)
    print('config loaded')

    # todo init http request handler

    # todo init gpio drivers



main()
