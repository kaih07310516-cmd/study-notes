height = float(input("请输入你的身高（m）："))
weight = float(input("请输入你的体重（kg）："))
BMI = weight / height ** 2
print(f"你的BMI为指数为{BMI:.2f}")
if BMI < 18.5:
    print("你的体重偏低，多补充营养")
elif 18.5 <= BMI < 24:
    print("你的体重正常，继续保持")
elif BMI >= 24:
    print("你的体重已超重，请控制饮食并进行适当锻炼")