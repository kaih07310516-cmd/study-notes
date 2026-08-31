count = 0
sum = 0
while True:
    value = input("Enter a number:")
    if value == 'Done':
        break
    try:
        number = float(value)
    except:
        print('please input number')
        continue
    count = count+1
    sum = sum + number
if count > 0:
    print(count,sum,sum / count)
else:
    print('没有输入数字')