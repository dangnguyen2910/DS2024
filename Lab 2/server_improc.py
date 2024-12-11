from xmlrpc.server import SimpleXMLRPCServer
from PIL import Image
import base64
from io import BytesIO

def convert_to_grayscale(encoded_image):
    image_data = base64.b64decode(encoded_image)
    image = Image.open(BytesIO(image_data))
    grayscale_image = image.convert('L')
    buffer = BytesIO()
    grayscale_image.save(buffer, format='PNG')
    buffer.seek(0)
    encoded_gray_image = base64.b64encode(buffer.read()).decode()
    return encoded_gray_image

server = SimpleXMLRPCServer(('localhost', 8000))
server.register_function(convert_to_grayscale, 'convert_to_grayscale')
print("server is running...")
server.serve_forever()