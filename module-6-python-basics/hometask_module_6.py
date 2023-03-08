
# declare and set main function
def main():
    import os
    import sys

    # import modules from python packages
    from ClassesModule import Publication
    from ClassesModule import FileModule

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

    if choice == '1':
        # declare and set variable with path, where output file should be created/saved/add data to file
        path = 'newsfeed.txt'
        # mode in which file will be opened
        # 'a' - add data to end of the file
        mode = 'a'
        while True:
            # use loop while to repeat input in case when user made a mistake with the input
            while True:
                try:
                    choice_u = input("\n--------------What post do you want to add? Please, choose: "
                                     "\n1 - News\n2 - Advertising\n3 - Movie of the day\n4 - Exit the program\n")
                    if choice_u not in ['1', '2', '3', '4']:
                        raise Exception("\n---------------------You must enter a number (1 or 2 or 3). "
                                        "Press 4 to exit.----------------\n")
                except Exception as err:
                    print(err)
                    continue  # We repeat the entry, if the entered is not a number from '1', '2', '3', '4'
                # Exit the loop if the numbers are entered correctly
                break
            if choice_u == '4':
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
            # repeat the entry if user wants to add one more publication
            continue

    if choice == '2':
        print('--------File input completed--------')

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


