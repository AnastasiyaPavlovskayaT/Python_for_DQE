
# declare and set main function
def main():
    # import modules from pyrhon packages
    from ClassesModule import Publication
    from ClassesModule import FileModule

    # set paths to files
    path_to_input_file = 'IncomingFile.txt'
    path_to_output_file = 'newsfeed.txt'

    # create FileTXT objects
    input_file = FileModule.FileTXT(path_to_input_file)
    output_file = FileModule.FileTXT(path_to_output_file)

    # parse incoming file and put content in to file with news feed
    output_file.write_list_to_file(Publication.PublicationIdentifier.publish_to_file(input_file.read_by_line()))
    # remove incoming file
    input_file.file_remove()

# main function call
# __name__ stores the name of the program
# __main__ indicates the scope where the code will be executed
if __name__ == "__main__":
    main()
