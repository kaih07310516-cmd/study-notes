import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

print("Creating JSON output on spider.js...")
howmany  = int(input('How many nodes?'))

cur.execute('''SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url 
    FROM Pages JOIN Links ON Pages.id = Links.to_id
    WHERE html IS NOT NULL AND ERROR IS NULL
    GROUP BY id ORDER BY id,inbound''')
