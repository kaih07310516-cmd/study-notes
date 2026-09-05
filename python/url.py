import urllib.request,urllib.parse,urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

count = dict()
for line in fhand:
    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word,0)+1
print(count)


f = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

for l in f:
    print(l.decode().strip())