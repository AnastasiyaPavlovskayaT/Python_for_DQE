
# declare and set class FileTXT
class FileTXT:
    # class attributes
    filepath = ''

    # class constructor
    # contain validation on the file type
    def __init__(self, filepath=''):
        self.filepath = filepath
        try:
            if not self.filepath.endswith('.txt'):
                raise NameError("File must be a '.txt' extension")
        except NameError as err:
            print(err)

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

    # declare and set method to write string in to the file
    def write_list_to_file(self, list_to_write):
        import os
        for string in list_to_write:
            with open(self.filepath, 'a') as file:
                file.write(string)
            file.close()

    # declare and set method to remove file
    def file_remove(self):
        import os
        os.remove(self.filepath)
