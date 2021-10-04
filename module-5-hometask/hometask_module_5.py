
# The Python script to solve Module 5 'Classes. OOP' home task.


# declare and set parent class Publication
class Publication:
    # class attributes
    postContent = ''
    postDate = ''

    # class constructor
    def __init__(self):
        pass

    # declare and set method to set content of publication by user using console input
    def set_post_data(self):
        post = input('\n--------------News publication.--------------\n')
        self.postContent = post

    # declare and set method to return publication content
    def publish(self, type_public):
        return self.postContent

    # declare and set protected method to save publication date
    def _publish_date(self):
        from datetime import datetime
        self.PostDate = datetime.now().strftime("%d/%m/%Y %H.%M")
        return datetime.now().strftime("%d/%m/%Y %H.%M")


# declare and set child class News
class News(Publication):
    # class attributes
    newsTown = ''

    # class constructor
    def __init__(self):
        Publication.__init__(self)

    # declare and set method to set content of news by user using console input
    def set_news_data(self):
        news = input('\n--------------News publication. Enter news: --------------\n')
        town = input('\n--------------News publication. Enter town: --------------\n')
        self.postContent = news
        self.newsTown = town

    # declare and set method to return news content
    def publish(self):
        self.postDate = self._publish_date()
        return 'News ------------------------\n' + self.postContent + '\n' + self.newsTown + ', ' + self.postDate + \
               '\n-----------------------------\n'


# declare and set child class Advertising
class Advertising(Publication):
    # class attributes
    expiredDate = ''

    # class constructor
    def __init__(self):
        Publication.__init__(self)

    # declare and set method to set content of advertising by user using console input
    def set_ad_data(self):
        adv = input('\n--------------Ad publication--------------\nEnter ad: ')
        self.postContent = adv

    # declare and set method to return advertising content
    def publish(self):
        self.postDate = self._publish_date()
        return 'Private Ad ------------------\n' + self.postContent + '\n' + 'Actual until: ' + self._days_left() + \
               ' days left\n-----------------------------\n'

    # declare and set protected (visible only for related classes) method
    # to set expired date of advertising by user using console input
    # input string is validated if is date and if the date in past
    def _expired_date(self):
        from datetime import datetime
        # use loop while to repeat input
        while True:
            user_date = input('------------Enter expired date (m/dd/yyyy):------------\n')
            try:
                date = datetime.strptime(user_date, '%m/%d/%Y')
                current_date = datetime.now()
                if date < current_date:
                    print("------------Entered date in the past. Please enter expired date once again.------------")
                    # repeat the entry, if the entered date in the past
                    continue
                # Exit the loop if the date is entered correctly
                break
            except ValueError:
                print('------------Invalid date!------------')
                # repeat the entry, if the entered string not thr date in asked format
                continue
        self.expiredDate = user_date

    # declare and set protected (visible only for related classes) method
    # to count of days that left for expired date
    def _days_left(self):
        from datetime import datetime
        self._expired_date()
        days_left = datetime.strptime(self.expiredDate, "%d/%m/%Y") - datetime.now()
        return self.expiredDate + ', ' + str(days_left.days)


# declare and set child class MovieOfTheDay
class MovieOfTheDay(Publication):
    # class attributes
    estimate = ''

    # class constructor
    def __init__(self):
        Publication.__init__(self)

    # declare and set private (visible only for MovieOfTheDay class) class method to random estimate for the movie
    def __estimate(self):
        import random
        movie_estimate = random.randint(1, 10)
        self.estimate = str(movie_estimate)

    # declare and set method to set content of movie by user using console input
    def set_movie_data(self):
        movie = input('\n--------------Movie of the day publication--------------\nEnter movie of the day: ')
        self.postContent = movie

    # declare and set method to return movie content
    def publish(self):
        self.postDate = self._publish_date()
        self.__estimate()
        return 'Movie of the Day --------------\n' + self.postContent + '\n' + self.postDate + '. Estimation: ' \
               + self.estimate + '\n------------------------------\n'


# declare and set main function
def main():
    import os
    import sys
    # declare and set variable with path, where output file should be created/saved/add data to file
    path = 'newsfeed.txt'
    # mode in which file will be opened
    # 'a' - add data to end of the file
    mode = 'a'
    # use loop while to repeat input
    while True:
        # use loop while to repeat input in case when user made a mistake with the input
        while True:
            try:
                choice = input("\n--------------What post do you want to add? Please, choose: \n1 - News\n2 - "
                               "Advertising\n3 - Movie of the day\n4 - Exit the program\n")
                if choice not in ['1', '2', '3', '4']:
                    raise Exception("\n---------------------You must enter a number (1 or 2 or 3). "
                                    "Press 4 to exit.----------------\n")
            except Exception as err:
                print(err)
                continue  # We repeat the entry, if the entered is not a number from '1', '2', '3', '4'
            # Exit the loop if the numbers are entered correctly
            break
        if choice == '4':
            print('\n-----------------Exit the program------------------\n')
            # method to exit from program
            sys.exit()
        # create/open file located by path in 'a' mode - add data to end of the file
        with open(path, mode) as f:
            if choice == '1':
                # create News class object
                news = News()
                # calling a method for user input
                news.set_news_data()
                # writing a publication to a file using  the publish method
                f.write(str(news.publish()) + '\n')
                # close the file
                f.close()
            elif choice == '2':
                # create Advertising class object
                adv = Advertising()
                # calling a method for user input
                adv.set_ad_data()
                # writing a publication to a file using  the publish method
                f.write(str(adv.publish()) + '\n')
                # close the file
                f.close()
            elif choice == '3':
                # create MovieOfTheDay class object
                movie = MovieOfTheDay()
                # calling a method for user input
                movie.set_movie_data()
                # writing a publication to a file using  the publish method
                f.write(str(movie.publish()) + '\n')
                # close the file
                f.close()
        # repeat the entry if user wants to add one more publication
        continue


# main function call
# __name__ stores the name of the program
# __main__ indicates the scope where the code will be executed
if __name__ == "__main__":
    main()
