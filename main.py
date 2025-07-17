import tkinter as tk 
from PIL import Image, ImageTk

class VirtuPet():
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-transparentcolor", "white")

        self.canvas = tk.Canvas(self.root, width=128, height=128, bg='white', highlightthickness=0)
        self.canvas.pack()

        self.pet_image = ImageTk.PhotoImage(Image.open("cat.png"))
        self.canvas.create_image(64, 64, image=self.pet_image)

        self.root.geometry(f"-100-100")

        self.canvas.bind("<ButtonPress-1>", self.start_move)
        self.canvas.bind("<B1-Motion>", self.do_move)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y
    
    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.x - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    pet = VirtuPet()
    pet.run()