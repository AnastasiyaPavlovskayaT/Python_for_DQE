# declare and set main function

def main():
    import os
    import sys
    import re

    # import modules from pyrhon packages
    from ClassesModule import Publication
    from ClassesModule import InputFile
    from ClassesModule import FileToCSV
    from ClassesModule import DBclass

    # create db class object
    db = DBclass.DBclass('newsfeed.db')
    # call db method to create db tables
    db.DB_tables_create()

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
        # print db tables result
        db.print_db_tables()
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
                # print db tables result
                db.print_db_tables()
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
                    # insert input record in db table
                    db.insert_news(news.postContent, news.newsTown, str(news.postDate))
                elif choice_u == '2':
                    # create Advertising class object
                    adv = Publication.Advertising()
                    # calling a method for user input
                    adv.set_ad_user_data()
                    # writing a publication to a file using  the publish method
                    f.write(str(adv.publish_user_input()) + '\n')
                    # close the file
                    f.close()
                    # insert input record in db table
                    db.insert_ad(adv.postContent, str(adv.expiredDate), adv._days_left()[1])
                elif choice_u == '3':
                    # create MovieOfTheDay class object
                    movie = Publication.MovieOfTheDay()
                    # calling a method for user input
                    movie.set_movie_user_data()
                    # writing a publication to a file using  the publish method
                    f.write(str(movie.publish()) + '\n')
                    # close the file
                    f.close()
                    # insert input record in db table
                    db.insert_movie(movie.postContent, str(movie.postDate), movie.estimate)

                # put the statistic for output file in the csv files
                FileToCSV.txt_to_csv(path)
            # repeat the entry if user wants to add one more publication
            continue

    if choice == '2':
        output_file = InputFile.FileTXT(path)
        while True:
            try:
                type_of_file = input("\n--------------Which type file? Please, choose: \n1 - TXT\n2 - "
                                     "JSON\n3 - XML\n0 - Exit the program\n")
                if type_of_file not in ['1', '2', '3', '0']:
                    raise Exception("\n---------------------You must enter a number (1 or 2 or 3). "
                                    "Press 0 to exit.----------------\n")
            except Exception as err:
                print(err)
                continue  # We repeat the entry, if the entered is not a number from '1', '2', '0'
            # Exit the loop if the numbers are entered correctly
            break
        if type_of_file == '1':
            # txt file object create
            txt_input_file = InputFile.FileTXT()
            txt_input_file.file_validation_input('.txt')

            # parse incoming file and put content in to file with news feed
            output_file.write_list_to_file(Publication.PublicationIdentifier.publish_to_file(txt_input_file.read_by_line()))
            for string in txt_input_file.read_by_line():
                if string[0] == 'News':
                    news = Publication.News()
                    news.set_news_data(string[1], string[2])
                    news.publish()
                    # insert input record in db table
                    db.insert_news(news.postContent, news.newsTown, str(news.postDate))
                if string[0] == 'Ad':
                    adv = Publication.Advertising()
                    adv.set_ad_data(string[1], string[2])
                    adv.publish()
                    # insert input record in db table
                    db.insert_ad(adv.postContent, str(adv.expiredDate), adv._days_left()[1])
                if string[0] == 'Movie':
                    movie = Publication.MovieOfTheDay()
                    movie.set_movie_data(string[1])
                    movie.publish()
                    # insert input record in db table
                    db.insert_movie(movie.postContent, str(movie.postDate), movie.estimate)
            # remove incoming file
            # txt_input_file.file_remove()

        if type_of_file == '2':
            # json file object create
            json_input_file = InputFile.FileJSON()
            json_input_file.file_validation_input('.json')

            # parse incoming file and put content in to file with news feed
            output_file.write_list_to_file(Publication.PublicationIdentifier.publish_to_file(json_input_file.read_by_line()))
            for string in json_input_file.read_by_line():
                if string[0] == 'News':
                    news = Publication.News()
                    news.set_news_data(string[1], string[2])
                    news.publish()
                    # insert input record in db table
                    db.insert_news(news.postContent, news.newsTown, str(news.postDate))
                if string[0] == 'Ad':
                    adv = Publication.Advertising()
                    adv.set_ad_data(string[1], string[2])
                    adv.publish()
                    # insert input record in db table
                    db.insert_ad(adv.postContent, str(adv.expiredDate), adv._days_left()[1])
                if string[0] == 'Movie':
                    movie = Publication.MovieOfTheDay()
                    movie.set_movie_data(string[1])
                    movie.publish()
                    # insert input record in db table
                    db.insert_movie(movie.postContent, str(movie.postDate), movie.estimate)
            # remove incoming file
            # json_input_file.file_remove()

        if type_of_file == '3':
            # xml file object create
            xml_input_file = InputFile.FileXML()
            xml_input_file.file_validation_input('.xml')
            # parse incoming file and put content in to file with news feed
            output_file.write_list_to_file(Publication.PublicationIdentifier.publish_to_file(xml_input_file.read_by_line()))
            for string in xml_input_file.read_by_line():
                if string[0] == 'News':
                    news = Publication.News()
                    news.set_news_data(string[1], string[2])
                    news.publish()
                    # insert input record in db table
                    db.insert_news(news.postContent, news.newsTown, str(news.postDate))
                if string[0] == 'Ad':
                    adv = Publication.Advertising()
                    adv.set_ad_data(string[1], string[2])
                    adv.publish()
                    # insert input record in db table
                    db.insert_ad(adv.postContent, str(adv.expiredDate), adv._days_left()[1])
                if string[0] == 'Movie':
                    movie = Publication.MovieOfTheDay()
                    movie.set_movie_data(string[1])
                    movie.publish()
                    # insert input record in db table
                    db.insert_movie(movie.postContent, str(movie.postDate), movie.estimate)

             # remove incoming file
             # xml_input_file.file_remove()


    # put the statistic for output file in the csv files
    FileToCSV.txt_to_csv(path)
    print('--------File input completed. Exit the program--------')

    # print db tables result
    db.print_db_tables()



# main function call
# __name__ stores the name of the program
# __main__ indicates the scope where the code will be executed
if __name__ == "__main__":
    main()
