import sqlite3
import datetime

DB = 'db.sqlite3'
APP = 'school'
MIG = '0001_initial'

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute('''SELECT COUNT(*) FROM django_migrations WHERE app=? AND name=?''', (APP, MIG))
count = cur.fetchone()[0]
if count == 0:
    cur.execute('''INSERT INTO django_migrations(app,name,applied) VALUES (?,?,?)''', (APP, MIG, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    print('inserted school.0001_initial into django_migrations')
else:
    print('school.0001_initial already recorded')
conn.close()
