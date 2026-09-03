counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('word:',words)

print('counting:')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('counts',counts)