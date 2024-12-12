import socket
import os

class Server:
    def __init__(self): 
        self.__port = 8080
        self.__host = 'localhost'
        self.__images = os.listdir('images')


    def run(self): 

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
            s.bind((self.__host, self.__port))
            print(f"Listening on {self.__host}:{self.__port}")

            while True: 
                s.listen()
                connection, client_address = s.accept()

                with connection: 
                    print(f"Connected by {client_address}")
                    requested_image = self.handle_request(connection)
                    self.send_image(requested_image, connection)
                    

    def handle_request(self, connection) -> "string": 
        while True: 
            request = connection.recv(1024)

            if not request: 
                break 

            requested_image = os.path.join('data', self.__images[request.decoce()])
                
        return requested_image
    

    def send_image(self, requested_image, connection): 
        with open(requested_image, 'rb') as image: 
            while (chunk := image.read(1024)):
                connection.sendall(chunk)
   



if __name__ == '__main__': 
    server = Server()
    server.run()
