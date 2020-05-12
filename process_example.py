from multiprocessing import Process # Can also use pool
import sqlite3
import os

print('Parent process %s.' % os.getpid())

conn = sqlite3.connect('process_test.sqlite')
c = conn.cursor()

# Drop table if exist
c.execute("DROP TABLE IF EXISTS Foo")

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS Foo
             (id INTEGER PRIMARY KEY, fakeid INTEGER)''')

conn.close()

ids = range(1000)
fakeids = range(0, 10000, 10)

def insert_data(i: int):
    print(f"Process {os.getpid()} started to insert data")

    conn = sqlite3.connect('process_test.sqlite')
    c = conn.cursor()
    num_entries = 1000 // 6
    for j in range(num_entries * i, num_entries * (i + 1)):
        t = (ids[j], fakeids[j])
        c.execute("INSERT INTO Foo VALUES (?, ?)", t)
        conn.commit()
    conn.close()

    print(f"Process {os.getpid()} finished")

processes = []
for i in range(6):
    p = Process(target=insert_data, args=(i,))
    processes.append(p)
    
for p in processes:
    p.start()

