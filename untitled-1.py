import sqlite3

with sqlite3.connect("test4.db") as connection:
    cursor = connection.cursor()
    
    query_1 = ''' 
               CREATE TABLE book (
                  id integer PRIMARY KEY AUTOINCREMENT,
                  title VARCHAR NOT NULL
                  )
            '''  
    cursor.execute(query_1)
    
    query_2 = '''
                 INSERT INTO book (title) 
                 VALUES ("Алиса в стране чудес"), ("Волшебники изумрудного города"), ("ОЗ - великий и ужасный")              
              '''
    cursor.execute(query_2)
    
    query_3 = ''' 
               CREATE TABLE auther (
                  id integer PRIMARY KEY AUTOINCREMENT,
                  surname VARCHAR NOT NULL,
                  name VARCHAR NOT NULL,
                  age CONSTRAINT ck_age CHECK (age>17)
                  )
            '''  
    cursor.execute(query_3)
    
    query_4 = '''
                 INSERT INTO auther (surname, name, age) 
                 VALUES ("Пушкин", "Александр", 22), ("Лермантов", "Михаил", 20), ("Толстой", "Лев", 28)              
              '''
    cursor.execute(query_4)    
    
    query_5 = ''' 
               CREATE TABLE book_auther (
                  id_book integer,
                  id_auther integer,
                  PRIMARY KEY (id_book, id_auther),
                  
                  FOREIGN KEY (id_book) REFERENCES book(id) ON DELETE SET NULL ON UPDATE CASCADE,
                  FOREIGN KEY (id_auther) REFERENCES auther(id) ON DELETE SET NULL ON UPDATE CASCADE
                  )
            '''  
    cursor.execute(query_5)
    
    query_6 = '''
                 INSERT INTO book_auther (id_book, id_auther) 
                 VALUES (1,1), (1,2), (2,3), (3,2)           
              '''
    cursor.execute(query_6)
    
    cursor.execute(''' 
                      SELECT book.title, auther.surname, auther.name
                      FROM book
                      INNER JOIN book_auther ON book.id = book_auther.id_book
                      INNER JOIN auther ON book_auther.id_book = auther.id
                   ''')
    
    for i in cursor.fetchall():
        print(*i)