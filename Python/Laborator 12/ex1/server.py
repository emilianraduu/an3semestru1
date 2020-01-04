import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",1234))
s.listen(1)
(connection,address) = s.accept()
number = ''
numbers = []
while True:
	data = connection.recv(1).decode("UTF-8")
	if not data: break
	if data == '|':
		numbers.append(int(number))
		number = ''
	else:
		number += data
	if "." in data:
		connection.send(str(sum(numbers)).encode("UTF-8"))
		break
connection.close()

