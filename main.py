import tkinter as tk
from PIL import Image, ImageTk

class VirtPet:
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

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    pet = VirtPet()
    pet.run()