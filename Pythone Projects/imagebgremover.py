from rembg import remove
from PIL import Image

# Input Image
input_path =  'F:/vscode1/img/Elon_Musk.png'

# Output Image
output_path = 'F:/vscode1/img/Elon_Musk_new.png'

# Open the image
input = Image.open(input_path)

# Removing the background
output = remove(input)

#Save the image
output.save(output_path)