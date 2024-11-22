import socket

HOST = '127.0.0.1'  
PORT = 65432
FILE_TO_SEND = 'file_to_send.txt'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")

    with open(FILE_TO_SEND, 'rb') as f:
        print(f'Sending {FILE_TO_SEND}...')
        while (chunk:= f.read(1024)):
            s.sendall(chunk)
    
print("File sent successfully.")
