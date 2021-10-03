


class Publication:
    postContent = ''
    postDate = ''

    def __init__(self):
        pass

    def setPostData(self):
        post = input('\n--------------News publication.--------------\n')
        self.postContent = post

    def publish(self, type_public):
        return self.postContent

    def _publish_date(self):
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y %H.%M")


class News(Publication):
    newsTown = ''
    def __init__(self):
        Publication.__init__(self)

    def publish(self):
        self.postDate = self._publish_date()
        return 'News -------------------------\n' + self.postContent + '\n' + self.newsTown + ', ' + self.postDate + '\n------------------------------\n'

    def setNewsData(self):
        news = input('\n--------------News publication. Enter news: --------------\n')
        town = input('\n--------------News publication. Enter town: --------------\n')
        self.postContent = news
        self.newsTown = town


class Advertising(Publication):
    def __init__(self):
        Publication.__init__(self)

    def setAdData(self):
        adv = input('\n--------------Ad publication--------------\nEnter ad: ')
        self.postContent = adv

    def publish(self):
        self.postDate = self._publish_date()
        return 'Private Ad ------------------\n' + self.postContent + '\n' + 'Actual until: ' + self._days_left() +' days left\n------------------------------\n'

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
        return user_date

    def _days_left(self):
        from datetime import datetime
        date = str(self._expired_date())
        days_left = datetime.strptime(date, "%d/%m/%Y") - datetime.now()
        return date +', ' + str(days_left.days)

class MovieOfTheDay(Publication):
    def __init__(self):
        Publication.__init__(self)

    def __estimate(self):
        import random
        estimate = random.randint(1,10)
        return estimate

    def setMovieData(self):
        movie = input('\n--------------Movie of the day publication--------------\nEnter movie of the day: ')
        self.postContent = movie

    def publish(self):
        self.postDate = self._publish_date()
        return 'Movie of the Day -------------------\n' + self.postContent + '\n' + self.postDate + '. Estimation: ' + str(self.__estimate()) + '\n------------------------------\n'

def main():
    import os
    import sys
    from sys import exit as sys_exit
    writepath = 'TEST.txt'
    mode = 'a' if os.path.exists(writepath) else 'w'
    while True:
        while True:
            try:
               choise = input("\n--------------What post do you want to add? Please, choose: \n1 - News\n2 - Advertising\n3 - Movie of the day\n4 - Exit the programm\n")
               if choise not in ['1', '2', '3', '4']:
                   raise Exception("\n---------------------You must enter a number (1 or 2 or 3). Press 4 to exit.----------------\n")
            except Exception as err:
               print(err)
               continue # We repeat the entry, if the entered is not a number from '1', '2', '3'
            # Exit the loop if the numbers are entered correctly
            break
        if choise == '4':
            print('\n-----------------Exit the programm------------------\n')
            sys.exit()
        with open(writepath, mode) as f:
            if choise == '1':
                news = News()
                news.setNewsData()
                f.write(str(news.publish()) + '\n')
            elif choise == '2':
                adv = Advertising()
                adv.setAdData()
                f.write(str(adv.publish()) + '\n')
            elif choise == '3':
                movie = MovieOfTheDay()
                movie.setMovieData()
                f.write(str(movie.publish()) + '\n')
        f.close()
        continue


if __name__ == "__main__":
    main()