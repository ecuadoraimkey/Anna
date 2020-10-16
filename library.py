import json
from anna import _anna_


class Library(object):

    def __init__(self):
        self.default_config = {}

        self.default_config['anna_version'] = 0.1
        self.default_config['library_path'] = 'library/'

        with open('anna_config.json', 'w') as config:
            json.dump(self.default_config, config)
