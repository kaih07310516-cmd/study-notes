const http = require('http');

const server = http.createServer((req, res) => {
  console.log(`[收到访问] 路径: ${req.url}`);

  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('欢迎来到首页！(状态码: 200)');
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('抱歉，你要找的资源不存在！(状态码: 404)');
  }
});

server.listen(3000, () => {
  console.log('服务器启动成功：http://localhost:3000');
});