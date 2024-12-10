import socket
import os
def receive_file(file_name, conn):
    with open(file_name, 'wb') as file:
        while True:
            data = conn.recv(1024)
            if data == b'END': 
                break
            file.write(data)
    print(f"File '{file_name}' : Got it babyy")

def send_file(file_name, conn):
    if not os.path.exists(file_name):
        conn.send(f"ERROR: File '{file_name}' not found.".encode('utf-8'))
        return
    conn.send(f"OK:{os.path.getsize(file_name)}".encode('utf-8')) 
    with open(file_name, 'rb') as file:
        while (data := file.read(1024)):
            conn.send(data)
    conn.send(b'END')  
    print(f"File '{file_name}' : sent boyyyy")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5000))
server_socket.listen(1)
print("Server listening on port 5000...")

conn, addr = server_socket.accept()
print(f"Connection from {addr}")

while True:
    command = conn.recv(1024).decode('utf-8') 
    if not command:
        break

    if command == "end-session":
        print("Ending session as requested by the client.")
        conn.send("Session closed.".encode('utf-8'))
        break

    elif command.startswith("send-file:"):
        file_name = command.split(":")[1]
        send_file(file_name, conn)

    elif command.startswith("receive-file:"):
        file_name = command.split(":")[1]
        receive_file(file_name, conn)

    else:
        conn.send("ERROR: Unknown command.".encode('utf-8'))

conn.close()
server_socket.close()
