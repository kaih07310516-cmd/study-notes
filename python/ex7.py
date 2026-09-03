filename = input('Enter file:')
if len(filename) < 1:filename = 'clown.txt'

filehand = open(filename)

many = dict()
for line in filehand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        many[w] =  many.get(w,0)+ 1

print(many)

largest = None
for key,value in many.items():
    print(key,value)
    if largest is None or largest < value:
        largest = value
print(largest)