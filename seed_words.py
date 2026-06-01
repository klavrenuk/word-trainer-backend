import json
import sqlite3

connection = sqlite3.connect("words.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY,
    word TEXT NOT NULL,
    translation TEXT NOT NULL,
    transcription TEXT
)
''')

with open('files/words.json', 'r', encoding='utf-8') as file:
    words = json.load(file)

for item in words:
    cursor.execute('''
        INSERT OR REPLACE INTO words (id, word, translation, transcription)
        VALUES (?, ?, ?, ?)
    ''', (
        item['id'],
        item['en'],
        item['ru'],
        item.get('tr', '')
    ))

connection.commit()
connection.close()

print(f'Загружено {len(words)} слов')