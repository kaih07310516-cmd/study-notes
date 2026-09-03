import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From',line):
        y = re.findall('^From (\S+@\S+)', line)
        print(line)
content = hand.read()
y = re.findall('^From (\S+@\S+)', content)
print(y)
x = 'My 2 favorite numbers are 3 and 15'
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[AEIOU]+',x)
print(y)
x = 'From: USing the: ,character'
y = re.findall('^F.+:',x)
print(y)
y = re.findall('^F.+?:',x)
print(y)