import urllib.request
import urllib.error
import time
from datetime import datetime
sites = [
    "https://www.baidu.com",
    "https://www.github.com",
    "https://this-site-does-not-exist-12345.com"
]
print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]开始检测\n")
for url in sites:
    start_time = time.time()
    try:
        req = urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=3)as resp:
            elapsed = round((time.time() - start_time)*1000,2)
            status = resp.getcode()
            result_msg = f"[OK]   {url} | 状态码: {status} | 耗时: {elapsed}ms"
    except urllib.error.HTTPError as e:
        result_msg = f"[WARN] {url} | HTTP错误: {e.code}"
    except Exception as e:
        result_msg = f"[FAIL] {url} | 无法连接: {type(e).__name__}"
    print(result_msg)
    with open("monitor.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat()} - {result_msg}\n")
    print('检测完成')