# testing some tkinter stuff
from tkinter import *
from PIL import ImageTk, Image

# Create a Tkinter window
root = Tk()
root.title("Image Viewer")

# Open an image file
image_path = "e1.jpg"  # Replace with your image path
img = Image.open(image_path)

# Optionally, resize the image
# img = img.resize((width, height), Image.ANTIALIAS)  # Replace width and height with desired size

# Create a PhotoImage object from the image
img_tk = ImageTk.PhotoImage(img)

# Create a label widget to display the image
label = Label(root, image=img_tk)
label.pack()

# Run the Tkinter event loop
root.mainloop()
