class Validation:
    isValidDate = False
    isPastDate = False
    isEmptyString = False

    def __init__(self):
        pass

    def is_date(self, user_date='1/1/2021'):
        from datetime import datetime
        if datetime.strptime(user_date, '%m/%d/%Y'):
            self.isValidDate = True
        return self.isValidDate

    def is_past_date(self, user_date='1/1/2021'):
        from datetime import datetime
        if elf.isDate(self, user_date) < datetime.now():
            self.isPastDate = True
        return self.isPastDate

    def is_empty_string(self, post=''):
        if post == '':
            self.isEmptyString = True
        return self.isEmptyString


class Publication:
    postContent = ''
    postDate = ''

    def __init__(self):
        pass

    def set_post_data(self):
        post = input('\n--------------News publication.--------------\n')
        self.postContent = post

    def publish(self, type_public):
        return self.postContent

    def _publish_date(self):
        from datetime import datetime
        self.PostDate = datetime.now().strftime("%d/%m/%Y %H.%M")
        return datetime.now().strftime("%d/%m/%Y %H.%M")


class News(Publication):
    newsTown = ''

    def __init__(self):
        Publication.__init__(self)

    def publish(self):
        self.postDate = self._publish_date()
        return 'News ------------------------\n' + self.postContent + '\n' + self.newsTown + ', ' + self.postDate + \
               '\n-----------------------------\n'

    def set_news_data(self):
        news = input('\n--------------News publication. Enter news: --------------\n')
        town = input('\n--------------News publication. Enter town: --------------\n')
        self.postContent = news
        self.newsTown = town


class Advertising(Publication):
    expiredDate = ''

    def __init__(self):
        Publication.__init__(self)

    def set_ad_data(self):
        adv = input('\n--------------Ad publication--------------\nEnter ad: ')
        self.postContent = adv

    def publish(self):
        self.postDate = self._publish_date()
        return 'Private Ad ------------------\n' + self.postContent + '\n' + 'Actual until: ' + self._days_left() + \
               ' days left\n-----------------------------\n'

    def _expired_date(self):
        from datetime import datetime
        current_datetime = datetime.now()
        while True:
            user_date = input('------------Enter expired date (m/dd/yyyy):------------\n')
            try:
                date = datetime.strptime(user_date, '%m/%d/%Y')
                current_date = datetime.now()
                if date < current_date:
                    print("------------Entered date in the past. Please enter expired date once again.------------")
                    continue
                break
            except ValueError:
                print('------------Invalid date!------------')
                continue
        self.expiredDate = user_date

    def _days_left(self):
        from datetime import datetime
        self._expired_date()
        days_left = datetime.strptime(self.expiredDate, "%d/%m/%Y") - datetime.now()
        return self.expiredDate + ', ' + str(days_left.days)


class MovieOfTheDay(Publication):
    estimate = ''

    def __init__(self):
        Publication.__init__(self)

    def __estimate(self):
        import random
        movie_estimate = random.randint(1, 10)
        self.estimate = str(movie_estimate)

    def set_movie_data(self):
        movie = input('\n--------------Movie of the day publication--------------\nEnter movie of the day: ')
        self.postContent = movie

    def publish(self):
        self.postDate = self._publish_date()
        self.__estimate()
        return 'Movie of the Day --------------\n' + self.postContent + '\n' + self.postDate + '. Estimation: ' \
               + self.estimate + '\n------------------------------\n'


def main():
    import os
    import sys
    path = 'newsfeed.txt'
    mode = 'a'  # if os.path.exists(path) else 'a'
    while True:
        while True:
            try:
                choice = input("\n--------------What post do you want to add? Please, choose: \n1 - News\n2 - "
                               "Advertising\n3 - Movie of the day\n4 - Exit the program\n")
                if choice not in ['1', '2', '3', '4']:
                    raise Exception("\n---------------------You must enter a number (1 or 2 or 3). "
                                    "Press 4 to exit.----------------\n")
            except Exception as err:
                print(err)
                continue  # We repeat the entry, if the entered is not a number from '1', '2', '3'
            # Exit the loop if the numbers are entered correctly
            break
        if choice == '4':
            print('\n-----------------Exit the program------------------\n')
            sys.exit()
        with open(path, mode) as f:
            if choice == '1':
                news = News()
                news.set_news_data()
                f.write(str(news.publish()) + '\n')
                f.close()
            elif choice == '2':
                adv = Advertising()
                adv.set_ad_data()
                f.write(str(adv.publish()) + '\n')
                f.close()
            elif choice == '3':
                movie = MovieOfTheDay()
                movie.set_movie_data()
                f.write(str(movie.publish()) + '\n')
                f.close()
        continue


if __name__ == "__main__":
    main()
