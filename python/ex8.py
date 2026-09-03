filename = input('Enter file:')
if len(filename) < 1:filename = 'clown.txt'

filehand = open(filename)

many = dict()
for line in filehand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        many[w] =  many.get(w,0)+ 1

tmp = dict()
newlist = list()
for key,value in many.items():
    tup = (value,key)
    newlist.append(tup)

cool = sorted(newlist,reverse=True)
print(cool)
for value,key in cool[ :5]:
    print((key,value))