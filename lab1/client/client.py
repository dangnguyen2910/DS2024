import socket 
import os 


class Client: 
    def __init__(self): 
        self.__port = 8006
        self.__host = 'localhost'


    def run(self): 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
            s.connect((self.__host, self.__port))
            print(f"Connected to server {self.__host}::{self.__port}")
            menu = s.recv(1024).decode()

            print(menu)

            while True: 
                user_input = input("Select image(or q:quit): ")

                if user_input == 'q': 
                    break

                s.sendall(user_input.encode())
                print("Send request")

                if not os.path.exists('images'): 
                    os.makedirs('images')

                with open('images/received_image.jpg', "wb") as f:
                    image_size = s.recv(7).decode()
                    image_size = int(image_size)

                    received_byte = 0
                    while received_byte < image_size: 
                        data = s.recv(1024)

                        if not data: 
                            break 
                        
                        received_byte += len(data)

                        f.write(data)


                


            



if __name__ == "__main__": 
    client = Client()
    client.run()