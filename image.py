import numpy as np
import cv2

PI = 3.14

class Image:

    #constructor setting values for image, rows, and columns attributes
    #and for printing out number of rows and columns
    def __init__(self, image):
        self.path = image
        self.image = cv2.imread(image,1)
        self.rows, self.columns = self.image.shape[:2]
        print(f"rows: {self.rows} columns: {self.columns}")

    #shows the image
    def show_image(self, title):
        cv2.imshow(title, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #reverts the image back to the original image. Necessary because some methods potentially cut parts of images off
    def revert_image(self):
        self.image = cv2.imread(self.path, 1)

    #translates the image
    def translate_image(self, xcoord, ycoord, number):
        matrix = np.array([[1, 0, xcoord], [0, 1, -ycoord]], dtype=float)
        self.image = cv2.warpAffine(self.image, matrix, (self.columns, self.rows)) #ycoord has to be
        #negative because OpenCV's coordinate system starts at top left corner
        self.show_image("Translated Image")

    #rotates the image by the degrees given by angle
    def rotate_image(self, angle):
        theta = angle * PI / 180 #degree to radian conversion
        rotation_matrix = np.array([[np.cos(theta),-np.sin(theta),0],
                                    [np.sin(theta),np.cos(theta),0],
                                    [0,0,1]],dtype=float)
        self.image = cv2.warpPerspective(self.image, rotation_matrix, (self.columns, self.rows))
        self.show_image("Rotated Image")

    # reflects the image over the x-axis
    def reflectx(self):
        # The matrix below is a transformation matrix. The negative 1 flips across the x-axis.
        matrix = np.array([[1, 0, 0], [0, -1, self.rows], [0, 0, 1]], dtype=float)
        self.image = cv2.warpPerspective(self.image, matrix, (self.columns, self.rows))
        self.show_image("Reflected Image")

    #reflects the image over the y-axis
    def reflecty(self):
        # The matrix below is a transformation matrix. The negative 1 flips across the x-axis.
        matrix = np.array([[-1, 0,self.columns],[0, 1, 0],[0, 0, 1]], dtype = float)
        self.image = cv2.warpPerspective(self.image, matrix,(self.columns,self.rows))
        self.show_image("Reflected Image")

    #crops the image by the number of pixels inputted by the user
    def crop_image(self, xcoord0, cropx, ycoord0, cropy):
        self.image = self.image[xcoord0:cropx, ycoord0:cropy]
        self.show_image("Cropped Image")

    #scales image by scalarx on x axis and scalary on y axis
    def scale_image(self, scalarx, scalary):
        self.image = cv2.resize(self.image, None, fx=scalarx, fy=scalary)
        self.show_image("Scaled Image")

    #shears the image in the x-direction by the inputted shearing factor
    def shearx(self, shearing_factor):
        matrix = np.array([[1, shearing_factor, 0], [0, 1, 0]])
        self.image = cv2.warpAffine(self.image, matrix, (self.image.shape[1], self.image.shape[0]))
        self.show_image("Sheared image")

    #shears the image in the y-direction by the inputted shearing factor
    def sheary(self, shearing_factor):
        matrix = np.array([[1, 0, 0], [shearing_factor, 1, 0]])
        self.image = cv2.warpAffine(self.image, matrix, (self.image.shape[1], self.image.shape[0]))
        self.show_image("Sheared Image")

    #This is the method that makes Funky Kong funky by making Funky Kong stand on top of Funky Kong
    #cuts the image in half, moves the upper half to the bottom and the lower half to the top
    def funky_kong(self):
        upper_half = self.image[:self.rows // 2, :]
        lower_half = self.image[self.rows // 2:, :]

        self.image = np.vstack((lower_half, upper_half))
        self.show_image("Extra Funky Funky Kong!")