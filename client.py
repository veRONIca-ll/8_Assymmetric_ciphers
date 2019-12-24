import socket
import pickle

def en_de_crypt(msg, key):
	secret = [chr(ord(msg[i])^key) for i in range(len(msg))]
	return ''.join(secret)

def send_(conn, msg, p_k):
	sock.send(pickle.dumps(en_de_crypt(msg, p_k)))

def recv_(conn, k):
	msg=en_de_crypt(pickle.loads(sock.recv(1024)), k)
	return msg

HOST = '127.0.0.1'
while True:										
	PORT=int(input('Enter port: '))
	if 1024<=PORT<=65525:
		break
	else:
		print('You made a mistake. Try again!')

sock = socket.socket()
sock.connect((HOST, PORT))

p, g, a = 7, 5, 3
A = g ** a % p
sock.send(pickle.dumps((p, g, A)))

B = pickle.loads(sock.recv(1024))

K = B ** a % p

msg = input('in> ')
while True: 
	try:
		if msg=='exit':
			break
		send_(sock, msg, K)
		print('out> ' + recv_(sock, K))
		msg=input('in> ')
	except:
		break

sock.close()
