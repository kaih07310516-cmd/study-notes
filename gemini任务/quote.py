import json
import urllib.request

url = "https://v1.hitokoto.cn/"
req = urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
try:
    with urllib.request.urlopen(req,timeout=5) as response:
        data = json.loads(response.read().decode("utf-8"))
        quote = data.get("hitokoto", "无")
        source = data.get("from", "?")
        print(quote)
        print(source)
except Exception as e:
    print(f"获取名言失败: {e}")