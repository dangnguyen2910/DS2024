import socket

HOST = '127.0.0.1'  
PORT = 65432         
FILE_TO_SAVE = 'received_file.txt'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with open(FILE_TO_SAVE, 'wb') as f:
            print(f"Receiving file and saving to: {FILE_TO_SAVE}")
            while True:
                data = conn.recv(1024)  
                if not data:  
                    break
                f.write(data)

    print("File received successfully.")
        