import socket,time
import json

key = 'nume'

file = open('./dict.json')
dict = json.load(file)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",1234))

s.send(str(dict).encode("UTF-8"))
s.send('|'.encode("UTF-8"))
s.send(key.encode("UTF-8"))
s.send('$'.encode("UTF-8"))
time.sleep(1)

message = s.recv(256).decode("UTF-8")
print(message)

s.close()

