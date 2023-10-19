import sqlite3

def connect_db():
    db = sqlite3.connect('users.db')
    return db

def sql_start():
    db = connect_db()
    cur = db.cursor()
    if db:
        print('Data Base connected')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS user_number('
        'tg_id TEXT PRIMARY KEY, '
        'username TEXT, '
        'created_at TEXT DEFAULT CURRENT_TIMESTAMP, '
        'full_name TEXT, '
        'birthday TEXT, '
        'phone_number TEXT, '
        'location TEXT, '
        'time TEXT, '
        'muolaja_turi TEXT'
        ')'
    )
    db.commit()

async def muolaja(state,city, muolaja_turi, time, full_name, birthday, phone_number, tg_id):
    db = connect_db()
    cur = db.cursor()
    async with state.proxy() as data:
        cur.execute(
            'UPDATE user_number SET location = ?, muolaja_turi = ?, time = ?, full_name = ?, birthday = ?, phone_number = ?, WHERE tg_id = ?',
            (city, muolaja_turi, time, full_name, birthday, phone_number, tg_id)
        )
        db.commit()
    print('Muolajaga yozildi')

def user_number():
    db = connect_db()
    cur = db.cursor()
    fetch = cur.execute('SELECT tg_id FROM user_number').fetchall()
    id = [i for i in fetch]
    return id


def add(tg_id, username, created_at):
    db = connect_db()
    cur = db.cursor()
    cur.execute('INSERT INTO user_number (tg_id, username, created_at) VALUES (?, ?, ?)', (tg_id, username, created_at))    
    db.commit()



