from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import random

QUOTES = [
    {"id": 1, "quote": "千里之行，始于足下。", "author": "老子"},
    {"id": 2, "quote": "Stay hungry, stay foolish.", "author": "Steve Jobs"},
    {"id": 3, "quote": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"}
]

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type","text/plain;charset=utf-8")
            self.end_headers()
            self.wfile.write("欢迎访问，请尝试请求/api/quote".encode("utf-8"))
        elif self.path == "/api/quote":
            self.send_response(200)
            self.send_header("Content-Type","application/json;charset=utf-8")
            self.send_header("Access-Control-Allow-Origin","*")
            self.end_headers()

            picked = random.choice(QUOTES)
            response_body = json.dumps(picked,ensure_ascii=False)
            self.wfile.write(response_body.encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-Type","text/plain;charset=utf-8")
            self.end_headers()
            self.wfile.write("404not found".encode("utf-8"))
if __name__=="__main__":
    server_address = ("127.0.0.1",8080)
    httpd = HTTPServer(server_address,SimpleAPIHandler)
    print("API服务已启动：http://127.0.0.1:8080")
    print("在浏览器或Postman访问：http://127.0.0.1：8080")
    httpd.serve_forever()

