Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

from rembg import remove
from PIL import Image
input_path = 'C:\Users\h04430\Desktop\py\FELV-cat.jpg'
output_path = 'C:\Users\h04430\Desktop\py\output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)