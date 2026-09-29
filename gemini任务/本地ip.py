import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"主机名: {hostname}")
print(f"本地局域网 IP: {local_ip}")