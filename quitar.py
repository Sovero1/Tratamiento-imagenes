from rembg import remove
from PIL import Image
input_path = r'C:\Users\h04430\Desktop\py\cat.jpg'
output_path = r'C:\Users\h04430\Desktop\py\output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)

