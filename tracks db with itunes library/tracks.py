import xml.etree.ElementTree as ET
import sqlite3

# connection = sqlite3.connect('tracks.sqlite')  # creates the database
# # database handler
# cursor = connection.cursor()
#
# # Make some fresh tables using executescript()
# cursor.executescript('''
# DROP TABLE IF EXISTS Artist;
# DROP TABLE IF EXISTS Album;
# DROP TABLE IF EXISTS Track;
# DROP TABLE IF EXISTS Genre;
#
# CREATE TABLE Artist (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Album (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     artist_id  INTEGER,
#     title   TEXT UNIQUE,
#     year   INTEGER
# );
#
# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY
#         AUTOINCREMENT UNIQUE,
#     title TEXT  UNIQUE,
#     album_id  INTEGER,
#     len INTEGER, rating INTEGER, count INTEGER, genre_id INTEGER
# );
#
# CREATE TABLE Genre (
#     id  INTEGER NOT NULL PRIMARY KEY
#         AUTOINCREMENT UNIQUE,
#     name TEXT
# );
# ''')

# <key>Name</key><string>Own It ft Ed Sheeran, Burna Boy[@music4Syte]</string>
# <key>Artist</key><string>Stormzy[@music4Syte]</string>
# <key>Album</key><string>Own It (feat. Ed Sheeran &#38; Burna Boy)</string>
# <key>Genre</key><string>Rap</string>
# <key>Year</key><integer>2019</integer>

fileName = input("Enter file name or location to file: ")
if len(fileName) < 1:
    fileName = 'Library.xml'


def lookup(dic, key):
    found = False
    for child in dic:
        if found:
            return child.text

        if child.tag == 'key' and child.text == key:
            found = True
    return None


try:
    stuff = ET.parse(fileName)
except Exception:
    print("Unable to read file", Exception)

all = stuff.findall('dict/dict/dict')
print('Dictionary Count:', len(all))

for entry in all:
    if lookup(entry, 'Track ID') is None:
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    year = lookup(entry, 'Year')

    if name is None or artist is None or album is None or genre is None:
        continue

    print(name, artist, album, count, rating, length, genre, year)

    # cursor.execute('''INSERT OR IGNORE INTO Artist (name)
    #         VALUES ( ? )''', (artist,))
    # cursor.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    # artist_id = cursor.fetchone()[0]
    #
    # cursor.execute('''INSERT OR IGNORE INTO Album (title, artist_id,year)
    #         VALUES ( ?, ?, ? )''', (album, artist_id, year))
    # cursor.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    # album_id = cursor.fetchone()[0]
    #
    # cursor.execute('''INSERT OR IGNORE INTO Genre (name)
    #             VALUES ( ? )''', (genre,))
    # cursor.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    # genre_id = cursor.fetchone()[0]
    #
    # cursor.execute('''INSERT OR REPLACE INTO Track
    #         (title, album_id, len, rating, count, genre_id)
    #         VALUES ( ?, ?, ?, ?, ?, ? )''',
    #                (name, album_id, length, rating, count, genre_id))
    #
    # connection.commit()
