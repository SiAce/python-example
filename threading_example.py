import threading
import sqlite3

conn = sqlite3.connect('test.sqlite')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE Foo
             (id INTEGER PRIMARY KEY, fakeid INTEGER)''')

conn.close()

ids = range(1000)
fakeids = range(0, 10000, 10)

def insert_data(i: int):
    conn = sqlite3.connect('test.sqlite')
    c = conn.cursor()
    num_entries = 1000 // 6
    for j in range(num_entries * i, num_entries * (i + 1)):
        t = (ids[j], fakeids[j])
        c.execute("INSERT INTO Foo VALUES (?, ?)", t)
        conn.commit()
    conn.close()

threads = []
for i in range(6):
    t = threading.Thread(target=insert_data, args=(i,))
    threads.append(t)
    
for t in threads:
    t.start()
