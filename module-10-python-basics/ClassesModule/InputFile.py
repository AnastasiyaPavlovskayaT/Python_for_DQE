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

    def file_validation_input(self, file_type):
        import re
        import os
        while True:
            try:
                path_to_input_file = str(input(
                    '\n---------Please, input name of the existing'+ file_type +' file with content. Press 0 to '
                    'exit.----------------\n'))
                if path_to_input_file == '0':
                    print('\n-----------------Exit the program------------------\n')
                    # method to exit from program
                    sys.exit()
                # validation on the file name
                if len(re.split(r'[~"#%&*:<>?/\\{|},]+', path_to_input_file)) > 1:
                    raise Exception('Invalid file name. File name should not contain ~"#%&*:<>?/\\{|},')
                # validation on the type of the file
                if not path_to_input_file.endswith(file_type):
                    raise Exception("--------------File must be a " + file_type + " --------------")
                # validation if the file exist
                if not os.path.exists(path_to_input_file):
                    raise Exception(
                        '-------The file with name ' + path_to_input_file + ' do not exist in the directory')
            except Exception as err:
                print(err)
                continue
            break
        self.filepath = path_to_input_file
        return path_to_input_file


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


class FileXML(InputFile):
    # class attributes
    filepath = ''

    # class constructor
    def __init__(self, filepath=''):
        InputFile.__init__(self, filepath)

    # declare and set method to parse incoming file
    # parsed strings saved in the list
    def read_by_line(self):
        import xml.etree.ElementTree as ET
        xml_file_p = ET.parse(self.filepath)
        root = xml_file_p.getroot()
        list_of_string = []
        list_of_content = []
        for root in root:
            for content in root.iter('content'):
                list_of_content = []
                list_of_content.append(root.attrib['type'])
                for data in content:
                    list_of_content.append(data.text)
                list_of_string.append(list_of_content)
        return list_of_string
