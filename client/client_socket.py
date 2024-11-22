import socket


def receive_data(data):
    pass

def send_data(file_path, client_socket):
    with open(file_path, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)



def main() -> None: 
    HOST = socket.gethostname()
    PORT = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Connected to server.")
    
    while True: 
        print("Options: ")
        print("1. Send data")
        print("2. Receive data")
        print("3. Quit")
        user_input = int(input("Choose: "))

        if (user_input == 1):
            send_data('dog.jpg', client_socket)
        elif (user_input == 2):
            receive_data()
        else: 
            client_socket.close()


if __name__ == '__main__':
    main()
