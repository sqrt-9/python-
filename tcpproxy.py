 import sys
 import socket
 import threading
 def server_loop(local_host,local_port,remote_host,remote_port,receive_first):
 	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		server.bind((local_host,local_port))
	except:
		print 'failed on %S:%d'%(local_host,local_port)
		print 'check for other'
		sys.exit(0)
	print 'listen on %s:%d'%(local_host,local_port)
	server.listen(5)
	while True:
		client_socket,addr = server.accept()
		print 'received from%s:%d'%(addr[0],addr[1])
		proxy_thread = threading.Thread(target = proxy_handler,args = (client_socket,remote_port,receive_first))
		proxy_thread.start()
def proxy_handler(client_socket,remote_host,remote_port,receive_first):
	remote_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	remote_socket.connect((remote_host,remote_port))
	if receive_first:
		remote_buffer = receive_from(remote_socket)
		hexdump(remote_buffer)
		remote_buffer = response_handler(remote_buffer)
		if len(remote_buffer):
			print 'send %d bytes to localhost'%len(remote_buffer)
			client_socket.send(remote_buffer)
	while True:
		local_buffer = receive_from(client_socket)
		if len(local_buffer):
		print 'received %d bytes from localhost'%len(local_buffer)
		hexdump(local_buffer)
		local_buffer = request_handler(local_buffer)
		remote_socket.send(local_buffer)
		print 'sent to remote'
	remote_buffer = receive_from(remote_sockeet)
	if len(remote_buffer):
		print 'received %d bytes from remote'%len(remote_buffer)
		hexdump(remote_buffer):
		remote_buffer = response_handler(remote_buffer)
		client_soket.send(remote_buffer)
		print 'sent to localhost'
	if not len(local_buffer) or not len(remote_buffer):
		client_socket.close()
		remote.socket.close()
		print 'no more date. Closing connections.'
		break
def hexdump(src,length = 16):
	result = []
	digits = 4 if isinstance(src,unicode) else 2
	for i in xrange(0,len(src,),length):
	s = src[i:i+length]
	hexa = b' '.join
def main():
	if len(sys.argv[1:]) != s:
		print 'example:127.0.0.1 9000 10.12.131.1 9000 True'
		sys.exit(0)
	local_host = sys.argv[1]
	local_port = int(sys.argv[2])
	remote_host = sys.argv[3]
	remote_port = int(sys.argv[4])
	receive_first = sys.argv[5]
	if 'True' in receive_first:
		receive_first = True
	else:
		receive_first = Flase
	server_loop(local_host,local_port,remote_host,remote_port,receive_first)

main()
