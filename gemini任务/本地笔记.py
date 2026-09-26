from datetime import datetime
note = input('输入内容：').split()
if not note :
    print('没有内容')
else:
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("note.txt","a",encoding="utf-8") as f:
        f.write(f"[{time}]{note}\n")