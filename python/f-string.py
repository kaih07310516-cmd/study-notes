#格式化输出（f-string)
name = "python sprinter"
day = 1
print(f"今天是{day}天，我是{name}，我要开始我的逆袭了。")
#字符串切片[start:stop:step]
s = "ABCDE12345"
print(s[0:3])
print(s[::-1])
print(s[::2])

#列表:有序
skills = ["Python","SQL","Django"]
skills.append("Redis")#添加元素
a = skills.append("Redis")
print(skills)
print(a)
print(skills[1])#访问第二个元素，0为1

#字典：键值对（Key-Value)
user_info = {"name":"hk","major":"cs","status":"Ready"}
print(user_info["major"])