import urllib.request
import json
import os
# 定义接口地址
api_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"

try:
    print("获取壁纸信息")
    req = urllib.request.Request(api_url,headers={'User-Agent':'Mozilla/5.0'})#网络请求
    with urllib.request.urlopen(req) as resp:
        # 发起网络连接，响应对象名称为resp
        data = json.loads(resp.read().decode('utf-8'))
        # 将返回的数据转存入data
        image_info = data['images'][0]
        # 将data中images第一项存入image_info
        img_url = 'https://cn.bing.com'+image_info['url']
        # 将image内url内容加上前缀连接成壁纸地址
        title = image_info.get('title','bing_wallpaper').strip().replace(" ","_")
        # 处理壁纸标题名称
        filename = f"{title}.jpg"
        print(f"今日壁纸:{title}")
        print("下载壁纸")
        img_req = urllib.request.Request(img_url,headers={"User-Agent":"Mozilla/5.0"})
        # 对刚刚获取的壁纸地址发起请求
        with urllib.request.urlopen(img_req) as img_resp,open(filename,'wb')as f:
            # 发起网络连接，响应对象名称为img_resp，创建filename文件简称为f
            f.write(img_resp.read())
            # 将获取到的写入f
        print(f"下载成功，文件位置：{os.path.abspath(filename)}")
except Exception as e:
    print(f"执行错误{e}")