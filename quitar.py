from rembg import remove
from PIL import Image
input_path = '..\Tratamiento-imagenes\cat.jpg'
output_path = '..\Tratamiento-imagenes\output2.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)

