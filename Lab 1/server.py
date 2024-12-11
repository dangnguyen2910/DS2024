import socket

host = '127.0.0.1'
port = 5000
file_send = r'D:\USTH\Nam Ba\Distributed System\dog.jpg'
file_receive = 'received.jpg'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print("Listening.....")
    conn, addr = s.accept()
    
    with conn:
        with open(file_send, 'rb') as file:
            while chunk := file.read(1024):
                conn.sendall(chunk)
        conn.shutdown(socket.SHUT_WR)

        with open(file_receive, 'wb') as file:
            while data := conn.recv(1024):
                file.write(data)
