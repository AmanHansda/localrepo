from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x830+-5+0")
        self.root.title("Face Recognition System")
        
        print("this is the starting!")
        heading = Label(root, text="The Boss", font=("Engravers MT", 40, "bold"), fg="black", bg="yellow")
        heading.pack(pady=20)  # Centered at the top with padding
        
        img1 = Image.open(r"C:\Users\amanh\Pictures\Saved Pictures\CUH\IMG_20231106_132028.jpg")
        img1 = img1.resize((500,700),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=15,y=100,width=500,height=700)
        
        
        
        img2 = Image.open(r"C:\Users\amanh\Pictures\Saved Pictures\CUH\WhatsApp Image 2025-01-26 at 21.37.31_4f7bbe89.jpg")
        img2 = ImageOps.exif_transpose(img2)
        img2 = img2.resize((500,700),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=515,y=100,width=500,height=700)
        
        
        img3 = Image.open(r"C:\Users\amanh\Pictures\Saved Pictures\CUH\IMG_20231103_095826.jpg")
        img3 = ImageOps.exif_transpose(img3)
        img3 = img3.resize((500,700),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1015,y=100,width=500,height=700)
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()