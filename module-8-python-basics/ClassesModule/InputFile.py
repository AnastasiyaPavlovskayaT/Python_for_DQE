# declare and set parent class for input files
class InputFile:
    # class attributes
    filepath = ''

    # class constructor
    def __init__(self, filepath=''):
        self.filepath = filepath

    # declare and set method to remove file
    def file_remove(self):
        import os
        os.remove(self.filepath)

    # declare and set method to write string in to the file
    def write_list_to_file(self, list_to_write):
        import os
        for string in list_to_write:
            with open(self.filepath, 'a') as file:
                file.write(string)
            file.close()


# declare and set child class FileTXT
class FileTXT(InputFile):
    # class attributes
    filepath = ''

    # class constructor
    def __init__(self, filepath=''):
        InputFile.__init__(self, filepath)

    # declare and set method to parse incoming file
    # parsed strings saved in the list
    def read_by_line(self):
        import os
        import re
        from ClassesModule import NormString
        list_of_string = []
        with open(self.filepath, 'r') as reader:
            # Read and print the entire file line by line
            line = reader.readline()
            while line != '':  # The EOF char is an empty string
                string = re.split(r'\\n', line)
                string[1] = NormString.normalize_string(string[1])
                if string[2]:
                    string[2] = string[2].capitalize()
                list_of_string.append(string)
                line = reader.readline()
            reader.close()
        return list_of_string


# declare and set child class FileJSON
class FileJSON(InputFile):
    # class attributes
    filepath = ''

    # class constructor
    def __init__(self, filepath=''):
        InputFile.__init__(self, filepath)

    # declare and set protected method to create list with the json values using keys
    @staticmethod
    def _feed_content_values(content_item={}):
        cont_list = [content_item['type']]
        for key in content_item['content']:
            cont_list.append(content_item['content'][key])
        return cont_list

    # declare and set method to parse incoming file
    # parsed strings saved in the list
    def read_by_line(self):
        import json
        import os
        with open(self.filepath, 'r') as json_file:
            raw_data = json.load(json_file)
            feed_content = raw_data['data']
            list_of_string = []
            for content_item in feed_content:
                list_of_string.append(FileJSON._feed_content_values(content_item))
        return list_of_string

