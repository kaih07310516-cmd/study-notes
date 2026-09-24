import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# 执行 SQL：从关系表 Links 中去重查询所有发出过链接的页面 ID（即投票发起人）
cur.execute('''SELECT DISTINCT from_id FROM Links''')
# 创建一个空列表，用来在内存中存储上述发链页面的 ID
from_ids = list()
# 遍历数据库游标返回的每一行查询结果
for row in cur:
    # row[0] 就是查出的 from_id，将其追加进 from_ids 列表中
    from_ids.append(row[0])
# 创建一个空列表，用来存储接收到链接的有效目标页面 ID（被投票人）
to_ids = list()
# 创建一个空列表，用来存储通过严格筛选后的合法连接关系对 (from_id, to_id)
links = list()
cur.execute('''SELECT DISTINCT from_id,to_id FROM Links ''')
#将清洗后的记录放入links
for row in cur:
    from_id = row[0]
    to_id = row[1]
    if from_id == to_id:
        continue
    if from_id not in from_ids:
        continue
    if to_id not in from_ids:
        continue
    links.append(row)
    if to_id not in to_ids:to_ids.append(to_id)

#用来存上一轮投票结果
prev_ranks = dict()
for node in from_ids:
    cur.execute('''SELECT new_rank FROM Pages WHERE id = ?''',(node,))
    row = cur.fetchone()
    prev_ranks[node] = row[0]

sval = input('How many iterations ')
many = 1
if (len(sval) > 0 ):
    many = int(sval)

if(len(prev_ranks) < 1):
    print("nothing ")
    quit()

for i in range(many):
    next_ranks = dict()
    total = 0.0
    for (node, old_rank) in list(prev_ranks.items()):
        total = total + old_rank
        next_ranks[node] = 0.0

    for (node,old_rank) in list(prev_ranks.items()):
        give_ids = list()
        for (from_id,to_id) in links:
            if from_id != node:
                continue
            if to_id not in to_ids:
                continue
            give_ids.append(to_id)
        if(len(give_ids) < 1):
            continue
        amount = old_rank / len(give_ids)

        for id in give_ids:
            next_ranks[id] = next_ranks[id] + amount

    newtot = 0
    for(node,next_rank)in list(next_ranks.items()):
        newtot = newtot + next_rank
    evap = (total - newtot)/ len(next_ranks)

    for node in next_ranks:
        next_ranks[node] = next_ranks[node] + evap

    newtot = 0
    for (node,next_rank)in list(next_ranks.items()):
        newtot = newtot +next_rank

    totdiff = 0
    for(node,old_rank) in list(prev_ranks.items()):
        new_rank = next_ranks[node]
        diff = abs(old_rank-new_rank)
        totdiff = totdiff + diff

    avediff = totdiff / len(prev_ranks)
    print(i+1,avediff)

    prev_ranks = next_ranks

print(list(next_ranks.items())[:5])
cur.execute('''UPDATE Pages SET old_rank = new_rank''')
for (id,new_rank) in list(next_ranks.items()):
    cur.execute('''UPDATE Pages SET new_rank = ? WHERE id=?''',(new_rank,id))
conn.commit()
cur.close()