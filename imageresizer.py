from PIL import Image
print('\nLets rezize the image\n')
name=input("Enter name of image = ")
img = Image.open(f'/Users/vedantkaushik/Downloads/{name}') # image extension *.png,*.jpg
new_width  = int(input('Enter new width = '))
new_height = int(input('Enter new height = '))
img = img.resize((new_width, new_height))
img.save(f'resized_{name}')



