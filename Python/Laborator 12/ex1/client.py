import socket,time

sum_list = [12, 25, 36, 48, 59]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",1234))

for i in sum_list:
	s.send(b'%d' %(i))
	s.send(b'|')


s.send(b".")

message = s.recv(256).decode("UTF-8")
print(message)
s.close()
