#the purpose of this program is to perform image transformations
#using matrices to make funky kong look funky(or any other character of your choice)

from image import Image
from selectFile import select_file

#uses select_file method to use a GUI to select the image
image = Image(select_file())

image.show_image("Image")

selection = 0
while selection < 500:
    print("select an option 1. Translate 2. Rotate 3. Reflect 4. Crop 5. Scale 6. Shear 7. Make Funky Kong Funky! 8. Exit")
    selection = int(input())

    #match statement to perform the desired action
    match selection:
        case 1: #translate
            xcoord = float(input("How many pixels do you want to translate in the x-direction?"))
            ycoord = float(input("How many pixels do you want to translate in the y-direction?"))
            image.translate_image(xcoord,ycoord,1)

        case 2: #rotate
            degrees = float(input("How many degrees do you want to rotate by?"))
            image.rotate_image(degrees) #explain how putting in different scalar factor can help

        case 3: #reflect
            choice = int(input("Do you want to reflect over the x-axis or y-axis?\n1. x-axis 2. y-axis"))
            if choice == 1:
                image.reflectx()
            elif choice == 2:
                image.reflecty()

        case 4: #crop
            xcoord0 = int(input("What do you want your starting index to be for cropping on the x-axis?"))
            cropx = int(input("How many pixels do you want to crop on the x-axis?"))
            ycoord0 = int(input("What do you want your starting index to be for cropping on the y-axis?"))
            cropy = int(input("How many pixels do you want to crop on the y-axis?"))
            image.crop_image(xcoord0, cropx, ycoord0, cropy)

        case 5: #scale
            scalarx = float(input("What do you want to be the scalar for the x-axis?")) #scalarx scales the image in the x direction
            scalary = float(input("What do you want to be the scalar for the y-axis?")) #scalary scales the image in the y direction
            image.scale_image(scalarx,scalary)

        case 6: #shear
            choice = int(input("Do you want to Shear in the x or y direction?\n1. x-direction 2. y-direction"))
            if choice == 1:
                shearing_factor = float(input("What do you want to be the shearing factor?"))
                image.shearx(shearing_factor)
            elif choice == 2:
                shearing_factor = float(input("What do you want to be the shearing factor?"))
                image.sheary(shearing_factor)

        case 7: #make funky kong funky
            image.funky_kong()

        case 8: #exit
            print("Exiting...")
            selection = 1000

        case _: #default case if invalid input
            print("Invalid selection")

    image.revert_image() #reverts image in case parts of image are cut off in transformation