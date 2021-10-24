
# set and declare class to work with database
class DBclass:
    # class attributes
    dbName = ''

    # class constructor
    def __init__(self, dbName = ''):
        self.dbName = dbName
        # pass
        # import sqlite3
        # with sqlite3.connect(self.dbName) as self.connection:
        #     self.cursor = self.connection.cursor()

    # private method to create connection with database
    def __connection(self, dbName = ''):
        import sqlite3
        with sqlite3.connect(self.dbName) as self.connection:
            self.cursor = self.connection.cursor()


    # method to create tables
    def DB_tables_create(self):
        self.__connection(self.dbName)
        try:
            # create NEWS table
            self.cursor.execute('CREATE TABLE NEWS ('
                           'id INT PRIMARY KEY, '
                           'content TEXT,'
                           'city TEXT,'
                           'publish_date TEXT)')
            self.connection.commit()
        except:
             self.connection.rollback()
        try:
            # create Ad table
            self.cursor.execute('CREATE TABLE AD ('
                           'id INT PRIMARY KEY, '
                           'ad TEXT,'
                           'expired_date TEXT,'
                           'days_left INT)')
            self.connection.commit()
        except:
            self.connection.rollback()
        try:
            # create Movie table
            self.cursor.execute('CREATE TABLE MOVIE ('
                           'id INT PRIMARY KEY, '
                           'movie TEXT,'
                           'publish_date TEXT,'
                           'estimation INT)')
            self.connection.commit()
        except:
            self.connection.rollback()

    # set and declare method to set last record id
    def set_id(self, table_name):
        try:
            self.cursor.execute(f'SELECT MAX(ID) FROM {table_name}')
            id = int(self.cursor.fetchall()[0][0]) + 1
        except:
            id = 1
        return id

    # method to insert content in the NEWS table
    # ''.format() is using to shielding ' (for example in input file exist 'it's')
    def insert_news(self, content, city, publish_date):
        self.__connection()
        id = self.set_id('NEWS')
        self.cursor.execute("SELECT COUNT(*) FROM NEWS WHERE content = ? AND city = ? ".format(), (content,city))
        if self.cursor.fetchall()[0][0] == 0:
            try:
                self.cursor.execute("INSERT INTO NEWS VALUES (?,?,?,?)".format(), (id, content, city, publish_date))
                self.connection.commit()
            except:
                self.connection.rollback()
                self.cursor.close()
        else:
            print('\n---------------------------------------DUPLICATE ROW--------------------------------------------------\n')
            print('-----Duplicate row. Was not recorded into database:----- \n', 'News: ' + content, ' \n', 'City: ' + city + '\n')
            self.connection.rollback()
            self.cursor.close()

    # method to insert content in the AD table
    # ''.format() is using to shielding ' (for example in input file exist 'it's')
    def insert_ad(self, content, expired_date, days_left):
        self.__connection()
        id = self.set_id('AD')
        self.cursor.execute("SELECT COUNT(*) FROM AD WHERE ad = ? AND expired_date = ?".format(), (content, expired_date))
        if self.cursor.fetchall()[0][0] == 0:
            try:
                self.cursor.execute("INSERT INTO AD VALUES (?,?,?,?)".format(), (id, content, expired_date, days_left))
                self.connection.commit()
            except:
                self.connection.rollback()
                self.cursor.close()
        else:
            print('\n---------------------------------------DUPLICATE ROW--------------------------------------------------\n')
            print('-----Duplicate row. Was not recorded into database:-----\n', 'Ad: ' + content, ' \n', 'Expired date: ' + expired_date + '\n')
            self.connection.rollback()
            self.cursor.close()

    # method to insert content in the MOVIE table
    # ''.format() is using to shielding ' (for example in input file exist 'it's')
    def insert_movie(self, content, publish_date, estimation):
        self.__connection()
        id = self.set_id('MOVIE')
        self.cursor.execute("SELECT COUNT(*) FROM MOVIE WHERE movie = ?".format(), (content,))
        if self.cursor.fetchall()[0][0] == 0:
            try:
                self.cursor.execute("INSERT INTO MOVIE VALUES (?,?,?,?)".format(), (id, content, publish_date, estimation))
                self.connection.commit()
            except:
                self.connection.rollback()
                self.cursor.close()
        else:
            print('\n---------------------------------------DUPLICATE ROW--------------------------------------------------\n')
            print('-----Duplicate row. Was not recorded into database:----- \n', 'Movie: ' + content, ' \n', 'Publish date: ' + publish_date + '\n')
            self.connection.rollback()
            self.cursor.close()

    # method to select data from db table
    def select(self, table_name):
        self.__connection()
        self.cursor.execute('SELECT * FROM {0}'.format(table_name))
        result = self.cursor.fetchall()
        for row in result:
            print(row)
        # print(result)
        self.cursor.close()

    # set an declare metod to put record content in the db tables
    def put_content_in_db(self, string):
        from ClassesModule import Publication
        if string[0] == 'News':
            news = Publication.News()
            news.set_news_data(string[1], string[2])
            news.publish()
            # insert input record in db table
            self.insert_news(news.postContent, news.newsTown, str(news.postDate))
        if string[0] == 'Ad':
            adv = Publication.Advertising()
            adv.set_ad_data(string[1], string[2])
            adv.publish()
            # insert input record in db table
            self.insert_ad(adv.postContent, str(adv.expiredDate), adv._days_left()[1])
        if string[0] == 'Movie':
            movie = Publication.MovieOfTheDay()
            movie.set_movie_data(string[1])
            movie.publish()
            # insert input record in db table
            self.insert_movie(movie.postContent, str(movie.postDate), movie.estimate)

    # method to print db tables in the consol
    def print_db_tables(self):
        print('-------------------------------------------NEWS TABLE----------------------------------------------------\n')
        self.select('NEWS')
        print('---------------------------------------------------------------------------------------------------------\n')
        print('--------------------------------------------AD TABLE-----------------------------------------------------\n')
        self.select('AD')
        print('---------------------------------------------------------------------------------------------------------\n')
        print('----------------------------------------- -MOVIE TABLE---------------------------------------------------\n')
        self.select('MOVIE')
        print('---------------------------------------------------------------------------------------------------------\n')