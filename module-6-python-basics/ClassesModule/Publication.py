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

    # declare and set method to set content
    def set_news_data(self, news='', town=''):
        from ClassesModule import NormString
        self.postContent = NormString.normalize_string(news)
        self.newsTown = NormString.normalize_string(town)

    # declare and set method to set content of news by user using console input
    def set_user_news_data(self):

        news = input('\n--------------News publication. Enter news: --------------\n')
        town = input('\n--------------News publication. Enter town: --------------\n')
        self.set_news_data(news, town)

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
    def set_ad_data(self,avd='',date=''):
        self.expiredDate = date
        self.postContent = avd

    def set_ad_user_data(self):
        from ClassesModule import NormString
        adv = input('\n--------------Ad publication--------------\nEnter ad: ')
        self.postContent = NormString.normalize_string(adv)

    # declare and set method to return advertising content
    def publish_user_input(self):
        self.postDate = self._publish_date()
        return 'Private Ad ------------------\n' + self.postContent + '\n' + 'Actual until: ' + self._days_left_user_input() + \
               ' days left\n-----------------------------\n'

    # declare and set protected (visible only for related classes) method
    # to count of days that left for expired date
    def _days_left(self):
        from datetime import datetime
        days_left = datetime.strptime(self.expiredDate, "%d/%m/%Y") - datetime.now()
        return self.expiredDate + ', ' + str(days_left.days)

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
    def _days_left_user_input(self):
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

    # declare and set method to set content of movie
    def set_movie_data(self,movie=''):
        self.postContent = movie

    # declare and set method to set content of movie by user using console input
    def set_movie_user_data(self):
        from ClassesModule import NormString
        movie = input('\n--------------Movie of the day publication--------------\nEnter movie of the day: ')
        self.postContent = NormString.normalize_string(movie)

    # declare and set method to return movie content
    def publish(self):
        self.postDate = self._publish_date()
        self.__estimate()
        return 'Movie of the Day --------------\n' + self.postContent + '\n' + self.postDate + '. Estimation: ' \
               + self.estimate + '\n------------------------------\n'

# declare and set class to return string related content type
class PublicationIdentifier:
    def __init__(self):
        pass

    @staticmethod
    def publish_to_file(list_of_string=[]):
        import os, re
        list_of_publications = []
        for string in list_of_string:
            if string[0] == 'News':
                news = News()
                news.set_news_data(string[1], string[2])
                list_of_publications.append(str(news.publish()) + '\n')
            if string[0] == 'Ad':
                adv = Advertising()
                adv.set_ad_data(string[1], string[2])
                list_of_publications.append(str(adv.publish()) + '\n')
            if string[0] == 'Movie':
                movie = MovieOfTheDay()
                movie.set_movie_data(string[1])
                list_of_publications.append(str(movie.publish()) + '\n')
        return list_of_publications