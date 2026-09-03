# 例子
# cabinet = dict()
# cabinet['summer'] = 12
# cabinet['fall'] = 3
# cabinet['spring'] = 75
# print(cabinet)
#
# cabinet['fall'] = cabinet['fall'] + 2
# print(cabinet)

# 字典计数
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
    # if name not in counts:
    # #     counts[name] = 1
    # # else:
    # #     counts[name] = counts[name] + 1
print(counts)