from itertools import cycle
from PIL import Image,ImageTk
import time
import tkinter as tk
root=tk.Tk()
root.title("image slide show")
image_path=[
    r'C:\Users\Dell\Desktop\python pro\proimg\61zQXxp4BEL._AC_UF894,1000_QL80_.jpg',
    r'C:\Users\Dell\Desktop\python pro\proimg\hot-anime-girl-mekuip4e4drhaxcl.jpg',
    r'C:\Users\Dell\Desktop\python pro\proimg\images.jpg',
    r"C:\Users\Dell\Desktop\python pro\proimg\sexy-anime-devil-girl-vector-600nw-2348492717.webp",
]
#resize the image
image_size=(300,300)
images=[Image.open(path). resize(image_size) for path in image_path]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label=tk.Label(root)
label.pack()

def  update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow=cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_path)):
        update_image()

play_button=tk.Button(root,text='play slideshow',command=start_slideshow)
play_button.pack()

root.mainloop()
