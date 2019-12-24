import socket
import pickle
import random


def en_de_crypt(msg, key):
	secret = [chr(ord(msg[i])^key) for i in range(len(msg))]
	return ''.join(secret)

def send_(conn, msg, p_k):
	conn.send(pickle.dumps(en_de_crypt(msg, p_k)))

def recv_(conn, k):
	msg=en_de_crypt(pickle.loads(conn.recv(1024)), K)
	return msg

HOST = '127.0.0.1'
sock = socket.socket()

port = 8080     		
while port!=65525:
	try:
		sock.bind(('',port))
		print('The port is {}'.format(port))
		break
	except:
		print('The port {} is not available. Checking new one...')
		port+=1

sock.listen(0)			
sock.setblocking(1)
conn, addr = sock.accept()

b = random.randint(1, 100)

msg = conn.recv(1024)
p, g, A = pickle.loads(msg)

B = g ** b %p
conn.send(pickle.dumps(B))

K = A ** b %p
while True:
	
	msg = recv_(conn, K)
	print(msg)
	send_(conn, 'понял принял', K)

conn.close()
