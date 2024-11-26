import socket

def receive_file(file_name, conn):
    with open(file_name, 'wb') as file:
        while True:
            data = conn.recv(1024)
            if data == b'END':  
                break
            file.write(data)
    print(f"File '{file_name}' received successfully.")


def send_file(file_name, conn):
    try:
        with open(file_name, 'rb') as file:
            conn.send(f"receive-file:{file_name}".encode('utf-8'))  
            while (data := file.read(1024)):
                conn.send(data)
        conn.send(b'END')  
        print(f"File '{file_name}' sent successfully.")
    except FileNotFoundError:
        print(f"ERROR: File '{file_name}' not found.")


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5000))
print("Connected to server.")


while True:
    print("\nOptions:")
    print("1. give a pedo")
    print("2. get a pedo")
    print("3. End session")
    choice = input("Enter your choice: ")

    if choice == "1":
        file_name = input("Enter the file name to send: ")
        send_file(file_name, client_socket)

    elif choice == "2":
        file_name = input("Enter the file name to request: ")
        client_socket.send(f"send-file:{file_name}".encode('utf-8'))  
        response = client_socket.recv(1024).decode('utf-8')
        if response.startswith("OK:"):
            file_size = int(response.split(":")[1])
            print(f"Receiving file of size {file_size} bytes...")
            receive_file(file_name, client_socket)
        else:
            print(response)

    elif choice == "3":
        client_socket.send("end-session".encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(response)
        break

    else:
        print("Invalid choice. Please try again.")

client_socket.close()
print("Connection closed.")
