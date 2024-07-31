# testing some tkinter stuff
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
# be aware that OS scaling will change the size of tkinter things

class App(tk.Frame):
    def chg_image(self):
        if self.im.mode == "1": # bitmap image
            self.img = ImageTk.BitmapImage(self.im, foreground="white")
        else:              # photo image
            self.img = ImageTk.PhotoImage(self.im)
            self.la.config(image=self.img, bg="#000000",
            width=self.img.width(), height=self.img.height())

    def open(self):
        filename = filedialog.askopenfilename(title="Choose image file")
        if filename != "":
            self.im = Image.open(filename)
        self.chg_image()
    
    def quit_app(self):
        self.master.quit()

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('Image Viewer')

        frame = tk.Frame(self)
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open...", command=self.open)
        file_menu.add_command(label="Quit", command=self.quit_app)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.master.config(menu=menu_bar)
        frame.pack(side=tk.BOTTOM, fill=tk.BOTH)

        self.la = tk.Label(frame)
        self.la.pack()

        self.pack()

if __name__ == "__main__":
    app = App(); app.mainloop()

