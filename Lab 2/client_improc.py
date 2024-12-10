import xmlrpc.client
from PIL import Image
import base64
from io import BytesIO

input_image_path = "dog.png"  
output_image_path = "grayscale_image.png"
proxy = xmlrpc.client.ServerProxy("http://localhost:8000")
with open(input_image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

encoded_gray_image = proxy.convert_to_grayscale(encoded_image)
gray_image_data = base64.b64decode(encoded_gray_image)
gray_image = Image.open(BytesIO(gray_image_data))
gray_image.save(output_image_path)

print(f"Grayscale image saved to {output_image_path}")