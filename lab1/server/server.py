import socket
import os

class Server:
    def __init__(self): 
        self.__port = 8006
        self.__host = 'localhost'
        self.__images = os.listdir('images')


    def run(self): 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
            s.bind((self.__host, self.__port))
            print(f"Listening on {self.__host}:{self.__port}")

            s.listen()

            connection, client_address = s.accept()

            print(f"Connected by {client_address}")

            # Send list of images
            menu = self.get_menu()
            connection.sendall(menu.encode())
            print('Send menu!')

            self.handle_request(connection)
                    
    
    def get_menu(self): 
        menu = ''
        for i, image_name in enumerate(self.__images):
            image_name = f'{i+1}. {image_name}\n'
            menu += image_name
        return menu


    def handle_request(self, connection) -> "string": 
        while True: 
            try: 
                request = connection.recv(1024).decode()
                print(f'Request {request}')
                
                if not request: 
                    break 
                
                idx = int(request) - 1

                requested_image = os.path.join('images', self.__images[idx])

                self.send_image(requested_image, connection)
                print("Send image!")
            except KeyboardInterrupt: 
                break
            except IndexError: 
                break
            

    def send_image(self, requested_image, connection): 

        with open(requested_image, 'rb') as image: 
            connection.sendall(f'{os.path.getsize(requested_image)}'.encode())

            while (chunk := image.read(1024)):
                connection.sendall(chunk)

            connection.sendall(b'EOF')
   



if __name__ == '__main__': 
    server = Server()
    server.run()
