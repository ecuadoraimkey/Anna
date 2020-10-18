import json
from os import listdir
from os.path import isfile, join


class Library(object):

    def __init__(self):
        self.default_config = {}

        self.default_config['anna_version'] = 0.1
        self.default_config['library_path'] = 'library/'

        with open('anna_config.json', 'w') as config:
            json.dump(self.default_config, config)
    
    def load_directory(self, dir_to_load):
        files_in_dir = [f for f in listdir(dir_to_load) if isfile(join(dir_to_load, f))]
        return files_in_dir