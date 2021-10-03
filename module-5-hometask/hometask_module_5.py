


class Publication:
    def __init__(self):
        pass

    def publish(self, type_public):
        return input('-------Enter post---------')

    def _publich_date(self):
        from datetime import datetime
        current_datetime = datetime.now()
        return str(current_datetime.day) + '/' + str(current_datetime.month) + '/' + str(current_datetime.year) + ' ' + str(current_datetime.hour) + '.' + str(current_datetime.minute)

    def _expired_date(self):
        from datetime import datetime
        current_datetime = datetime.now()
        while True:
            try:
                expired_date_day = int(input('Enter the expiration date of the end of the ad (day): '))
                expired_date_month = int(input('Enter the expiration date of the end of the ad (month): '))
                expired_date_year = int(input('Enter the expiration date of the end of the ad (year): '))
                date = str(expired_date_day) + '/' + str(expired_date_month) + '/' + str(expired_date_year)
                if expired_date_year < current_datetime.year or (expired_date_year == current_datetime.year and expired_date_month < current_datetime.month):
                    raise Exception("\n--------------------The date that was entered is in the past! Please try again.----------------------------\n")
                elif expired_date_year == current_datetime.year and expired_date_month < current_datetime.month:
                    raise Exception("\n--------------------The date that was entered is in the past! Please try again.----------------------------\n")
                elif expired_date_year == current_datetime.year and expired_date_month == current_datetime.month and expired_date_day < current_datetime.day:
                    raise Exception("\n--------------------The date that was entered is in the past! Please try again.----------------------------\n")
            except Exception as err:
                print(err)
                continue
            break
        return date

    def _days_left(self):
        from datetime import datetime
        date = str(self._expired_date())
        days_left = datetime.strptime(date, "%d/%m/%Y") - datetime.now()
        return date +', ' + str(days_left.days)


class News(Publication):
    def __init__(self):
        Publication.__init__(self)
    def publish(self):
        from datetime import datetime
        news = input('\n--------------News publication. Enter news: --------------\n')
        town = input('\n--------------News publication. Enter town: --------------\n')
        return 'News -------------------------\n' + news + '\n' + town + ', ' + self._publich_date() + '\n------------------------------\n'


class Advertising(Publication):
    def __init__(self):
        Publication.__init__(self)
    def publish(self):
        from datetime import datetime
        adv = input('\n--------------Ad publication--------------\nEnter ad: ')
        return 'Private Ad ------------------\n' + adv + '\n' + 'Actual until: ' + self._days_left() +' days left\n------------------------------\n'


class MovieOfTheDay(Publication):
    def __init__(self):
        Publication.__init__(self)

    def __estimate(self):
        import random
        estimate = random.randint(1,10)
        return estimate

    def publish(self):
        from datetime import datetime
        movie = input('\n--------------Movie of the day publication--------------\nEnter movie of the day: ')
        return 'Movie of the Day -------------------\n' + movie + '\n' + self._publich_date() + '. Estimation: ' + str(self.__estimate()) + '\n------------------------------\n'

def main():
    import os
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
               continue # Повторяем ввод, если введено не число из '1', '2', '3'
            # Выходим из цикла, если числа введены правильно
            break
        if choise == '4':
            print('\n-----------------Exit the programm------------------\n')
            sys.exit()
        with open(writepath, mode) as f:
            if choise == '1':
                news = News()
                f.write(str(news.publish()) + '\n')
            elif choise == '2':
                adv = Advertising()
                f.write(str(adv.publish()) + '\n')
            elif choise == '3':
                movie = MovieOfTheDay()
                f.write(str(movie.publish()) + '\n')
        f.close()
        continue


if __name__ == "__main__":
    main()