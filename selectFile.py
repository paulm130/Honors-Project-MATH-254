import tkinter
from tkinter import filedialog
import os

#uses the tkinter GUI to select a file
def select_file():
    root = tkinter.Tk()
    root.withdraw()
    folder = os.getcwd()

    file_path = filedialog.askopenfilename(
        title="Select an Image",
        initialdir = folder,
        filetypes=(
            ("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp"),  #Only allows the selection of an image
        ))

    return file_path