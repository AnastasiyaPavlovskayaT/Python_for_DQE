# declare and set main function
def main():
    import os
    import sys
    import re

    # import modules from pyrhon packages
    from ClassesModule import Publication
    from ClassesModule import FileModule
    from ClassesModule import FileToCSV
    from ClassesModule import JSONtoFile

    while True:
        try:
            choice = input("\n--------------Manual input or from file: \n1 - Manual input\n2 - "
                           "File input\n0 - Exit the program\n")
            if choice not in ['1', '2', '0']:
                raise Exception("\n---------------------You must enter a number (1 or 2 or 0). "
                                "Press 0 to exit.----------------\n")
        except Exception as err:
            print(err)
            continue  # We repeat the entry, if the entered is not a number from '1', '2', '3', '4'
        # Exit the loop if the numbers are entered correctly
        break

    if choice == '0':
        print('\n-----------------Exit the program------------------\n')
        # method to exit from program
        sys.exit()

    # declare and set variable with path, where output file should be created/saved/add data to file
    path = 'newsfeed.txt'

    if choice == '1':
        # mode in which file will be opened
        # 'a' - add data to end of the file
        mode = 'a'
        while True:
            # use loop while to repeat input in case when user made a mistake with the input
            while True:
                try:
                    choice_u = input("\n--------------What post do you want to add? Please, choose: \n1 - News\n2 - "
                                     "Advertising\n3 - Movie of the day\n0 - Exit the program\n")
                    if choice_u not in ['1', '2', '3', '0']:
                        raise Exception("\n---------------------You must enter a number (1 or 2 or 3). "
                                        "Press 0 to exit.----------------\n")
                except Exception as err:
                    print(err)
                    continue  # We repeat the entry, if the entered is not a number from '1', '2', '3', '4'
                # Exit the loop if the numbers are entered correctly
                break
            if choice_u == '0':
                print('\n-----------------Exit the program------------------\n')
                # method to exit from program
                sys.exit()
            # create/open file located by path in 'a' mode - add data to end of the file
            with open(path, mode) as f:
                if choice_u == '1':
                    # create News class object
                    news = Publication.News()
                    # calling a method for user input
                    news.set_user_news_data()
                    # writing a publication to a file using  the publish method
                    f.write(str(news.publish()) + '\n')
                    # close the file
                    f.close()
                elif choice_u == '2':
                    # create Advertising class object
                    adv = Publication.Advertising()
                    # calling a method for user input
                    adv.set_ad_user_data()
                    # writing a publication to a file using  the publish method
                    f.write(str(adv.publish_user_input()) + '\n')
                    # close the file
                    f.close()
                elif choice_u == '3':
                    # create MovieOfTheDay class object
                    movie = Publication.MovieOfTheDay()
                    # calling a method for user input
                    movie.set_movie_user_data()
                    # writing a publication to a file using  the publish method
                    f.write(str(movie.publish()) + '\n')
                    # close the file
                    f.close()
                FileToCSV.txt_to_csv(path)
            # repeat the entry if user wants to add one more publication
            continue

    if choice == '2':
        output_file = FileModule.FileTXT(path)
        while True:
            try:
                type_of_file = input("\n--------------Which type file? Please, choose: \n1 - TXT\n2 - "
                                     "JSON\n0 - Exit the program\n")
                if type_of_file not in ['1', '2', '0']:
                    raise Exception("\n---------------------You must enter a number (1 or 2). "
                                    "Press 0 to exit.----------------\n")
            except Exception as err:
                print(err)
                continue  # We repeat the entry, if the entered is not a number from '1', '2', '3', '4'
            # Exit the loop if the numbers are entered correctly
            break
        if type_of_file == '1':
            while True:
                try:
                    path_to_input_file = str(input(
                        '\n---------Please, input name of the existing .txt file with content. Press 0 to '
                        'exit.----------------\n'))
                    if path_to_input_file == '0':
                        print('\n-----------------Exit the program------------------\n')
                        # method to exit from program
                        sys.exit()
                    # validation on the file name
                    if len(re.split(r'[~"#%&*:<>?/\\{|},]+', path_to_input_file)) > 1:
                        raise Exception('Invalid file name. File name should not contain ~"#%&*:<>?/\\{|},')
                    # validation on the type of the file
                    if not path_to_input_file.endswith('.txt'):
                        raise Exception("--------------File must be a '.txt' --------------")
                    # validation if the file exist
                    if not os.path.exists(path_to_input_file):
                        raise Exception(
                            '-------The file with name ' + path_to_input_file + ' do not exist in the directory')
                except Exception as err:
                    print(err)
                    continue
                break
            # create txt file object
            input_file = FileModule.FileTXT(path_to_input_file)
            # parse incoming file and put content in to file with news feed
            output_file.write_list_to_file(Publication.PublicationIdentifier.publish_to_file(input_file.read_by_line()))
            # put the statistic for output file in the csv files
            FileToCSV.txt_to_csv(path)
            print('--------File input completed--------')
            # remove incoming file
            # input_file.file_remove()

        if type_of_file == '2':
            while True:
                try:
                    path_to_input_file = str(input(
                        '\n---------Please, input name of the existing .json file with content. Press 0 to '
                        'exit.----------------\n'))
                    if path_to_input_file == '0':
                        print('\n-----------------Exit the program------------------\n')
                        # method to exit from program
                        sys.exit()
                    # validation on the file name
                    if len(re.split(r'[~"#%&*:<>?/\\{|},]+', path_to_input_file)) > 1:
                        raise Exception('Invalid file name. File name should not contain ~"#%&*:<>?/\\{|},')
                    # validation on the type of the file
                    if not path_to_input_file.endswith('.json'):
                        raise Exception("--------------File must be a '.json' --------------")
                    # validation if the file exist
                    if not os.path.exists(path_to_input_file):
                        raise Exception(
                            '-------The file with name ' + path_to_input_file + ' do not exist in the directory')
                except Exception as err:
                    print(err)
                    continue
                break
            # create json file object
            json_file = JSONtoFile.FileJSON(path_to_input_file)
            # parse incoming file and put content in to file with news feed
            output_file.write_list_to_file(Publication.PublicationIdentifier.publish_to_file(json_file.read_by_line()))
            # put the statistic for output file in the csv files
            FileToCSV.txt_to_csv(path)
            print('--------File input completed--------')
            # remove incoming file
            # input_file.file_remove()


# main function call
# __name__ stores the name of the program
# __main__ indicates the scope where the code will be executed
if __name__ == "__main__":
    main()
