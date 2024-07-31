import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def add_images_to_frame(frame, image_paths, check_vars):
    for idy, image_path in enumerate(image_paths):
        img = Image.open(image_path)
        img = img.resize((100, 100))
        photo = ImageTk.PhotoImage(img)
        
        # Create a checkbutton with the image
        check_var = tk.IntVar()
        check_vars.append(check_var)
        check_button = tk.Checkbutton(frame, image=photo, variable=check_var)
        check_button.image = photo  # Keep a reference to avoid garbage collection
        check_button.grid(row=idy, column=0, sticky='news')
    frame.update_idletasks()



# Create the main application window
root = tk.Tk()
root.title("Selectable List of Images with Checkbuttons")
root.geometry("500x400")

root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Create a main frame
frame_main = tk.Frame(root, bg="gray")
frame_main.grid(sticky='news')

# Create a frame for the canvas with non-zero row&column weights
frame_canvas = tk.Frame(frame_main)
frame_canvas.grid(row=0, column=0, pady=(2, 0), sticky='nw')
frame_canvas.grid_rowconfigure(0, weight=1)
frame_canvas.grid_columnconfigure(0, weight=1)
# Set grid_propagate to False to allow 5-by-5 buttons resizing later
frame_canvas.grid_propagate(False)

# Add a canvas in that frame
canvas = tk.Canvas(frame_canvas, bg="yellow")
canvas.grid(row=0, column=0, sticky="news")

# Link a scrollbar to the canvas
vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)
# Set the canvas scrolling region
canvas.bind('<Configure>',
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame to contain the checkbuttons
frame_cbs = tk.Frame(canvas, bg="blue")
canvas.create_window((0, 0), window=frame_cbs, anchor='nw')

# List of image paths
image_paths = ["image1.png", "image2.png", "image3.png", "image4.png", "image5.png"]

# List to store checkbutton variables
check_vars = []

# Add image checkbuttons to the frame
add_images_to_frame(frame_cbs, image_paths, check_vars)

# Resize the canvas frame to show an image and the scrollbar
select_width = 128 # TODO make select button width if not adaptable
select_height = 370 # TODO fit to y height available
frame_canvas.config(width=select_width + vsb.winfo_width(),
                    height=select_height)

def get_selected_images():
    selected_indices = [idx for idx, var in enumerate(check_vars) if var.get() == 1]
    print(f"Selected image indices: {selected_indices}")
# Add a button to print the selected images
select_button = tk.Button(frame_main, text="Get Selected Images",
                          command=get_selected_images)
select_button.grid(row=1, column=0, pady=2)

# Run the application
root.mainloop()