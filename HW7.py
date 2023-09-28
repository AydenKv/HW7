import sqlite3


with sqlite3.connect('student.db') as student: # задание 1 и 2
    cursor_ = student.cursor()
    # задание 3
    cursor_.execute('''CREATE TABLE IF NOT EXISTS student(
    hobby TEXT,
    name TEXT,
    last_name TEXT,
    birth_year INTEGER,
    points INTEGER
    )''')
    student.commit()

    # задание 4
    # cursor_.execute('''INSERT INTO student VALUES ('q', 'wsx', 'qwerrrty', 2001, 19)''')
    # cursor_.execute('''INSERT INTO student VALUES ('w', 'asd', 'plkjhgbvfqq', 2002, 23)''')
    # cursor_.execute('''INSERT INTO student VALUES ('e', 'rty', 'lkmjnhbg', 2003, 1)''')
    # cursor_.execute('''INSERT INTO student VALUES ('r', 'fgh', 'lkmjnqw', 2004, 198)''')
    # cursor_.execute('''INSERT INTO student VALUES ('t', 'yui', 'uiqqw', 2005, 193)''')
    # cursor_.execute('''INSERT INTO student VALUES ('y', 'pow', 'lksjs', 2006, 14)''')
    # cursor_.execute('''INSERT INTO student VALUES ('u', 'khj', 'kojminhubgyu', 2007, 7)''')
    # cursor_.execute('''INSERT INTO student VALUES ('i', 'pls', 'qwesadwe', 2008, 4)''')
    # cursor_.execute('''INSERT INTO student VALUES ('o', 'lkj', 'kojminhuijmo', 2009, 12)''')
    # cursor_.execute('''INSERT INTO student VALUES ('p', 'fhg', 'vygbhu', 2010, 5)''')

    # задание 5
    cursor_.execute('''SELECT * FROM student''')
    item = cursor_.fetchall()
    for i in item:
        if len(i[2]) > 10:
            print(i)

    # задание 6
    cursor_.execute('''UPDATE student SET name="genius" WHERE points>10''')

    # задание 7
    for i in item:
        if i[1] == 'genius':
            print(i)

    cursor_.execute('''DELETE FROM student WHERE rowid % 2 == 0''')

