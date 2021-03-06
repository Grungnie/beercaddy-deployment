import os
import json


class JsonCache:
    def __init__(self, filename='cache.json', root_directory=None):
        if root_directory is not None:
            self.data_location = '{}/{}'.format(root_directory, filename)
        else:
            self.data_location = '{}/{}'.format(os.getcwd(), filename)

        # if the file doesn't exist create a empty file with a json object
        if not os.path.isfile(self.data_location):
            with open(self.data_location, 'w+') as data_file:
                data_file.write('{}')

    def get(self, key):
        with open(self.data_location) as data_file:
            data = json.load(data_file)
            if key in data:
                value = data[key]
            else:
                value = None

        return value

    def set(self, key, value):
        with open(self.data_location, 'r+') as data_file:
            data = json.load(data_file)

            data[key] = value

            data_file.seek(0)
            data_file.write(json.dumps(data))
            data_file.truncate()

        return True

    def delete(self, key):
        with open(self.data_location, 'r+') as data_file:
            data = json.load(data_file)

            if key not in data:
                return False

            data.pop(key, None)

            data_file.seek(0)
            data_file.write(json.dumps(data))
            data_file.truncate()

        return True