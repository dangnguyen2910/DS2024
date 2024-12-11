import socket
host = '127.0.0.1'
port = 5000
file_send = r'D:\USTH\Nam Ba\Distributed System\dog2.jpg'
file_receive = 'received1.jpg'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    with open(file_receive, 'wb') as file:
        while data := s.recv(1024):
            if not data:
                break
            file.write(data)

    with open(file_send, 'rb') as file:
        while chunk := file.read(1024):
            s.sendall(chunk)
    s.shutdown(socket.SHUT_WR)
