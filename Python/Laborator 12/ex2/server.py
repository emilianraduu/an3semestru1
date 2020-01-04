import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",1234))
s.listen(1)
(connection,address) = s.accept()
recv_str = ''
key_bool = False
key = ''
while True:
	data = connection.recv(1).decode("UTF-8")
	if data == '$':
		recv_str = recv_str.replace('\'', '\"')
		key = key.replace("|", "")
		obj = json.loads(recv_str)
		if key in obj:
			print(obj[key])
			connection.send(str(obj[key]).encode("UTF-8"))
			break
		else:
			print("No key found")
			connection.send("No key found".encode("UTF-8"))
			break
	else:
		if data == '|':
			key_bool = True
		if key_bool == False:
			recv_str += data
		else:
			key += data
connection.close()
