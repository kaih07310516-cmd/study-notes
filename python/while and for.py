# while True:
#     line = input('>')
#     if line == "Done":
#         break
#     print(line)
# print('Done')


for i in [5,4,3,2,1]:
    print(i)
print('Done')

friends = ['hk','hyx']
for friend in friends:
    print("hello,",friend)
print("Done")

numbers = [2,4,6,8,24,521,52,35,64]
large_n = -1
small_n = None
count = 0
sum = 0

for value in numbers:
    if small_n is None:
        small_n = value
    elif value < small_n:
        small_n = value

    if value > large_n:
        large_n = value
    sum = sum + value
    count = count +1
    average = sum / count
print("最大数为：",large_n,
      "最小数为：",small_n,
      "总和为：",sum,
      "循环了",count,"次",
      "平均数为：",average)

found = False
for value in numbers:
    if value  ==4:
        found = True
        break
print('该数组是否存在4：',found)