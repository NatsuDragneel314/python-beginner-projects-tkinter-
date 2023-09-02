from tkinter import filedialog
from tkinter import*
from PIL import Image
from tkinter import messagebox

root=Tk()
root.title("Image_converter")
root.geometry('400x260')

global img_1

def Choose_file():
    global img_1
    img=filedialog.askopenfilename()
    entry.delete(0,END)
    entry.insert(0,img)
    img_1=Image.open(img)
    

def convert1():
    global img_1
    img1=filedialog.asksaveasfilename(defaultextension='.png')
    img_1.save(img1)
    messagebox.showinfo("congrats", "Converted to PNG")

def convert2():
    global img_1
    img2=filedialog.asksaveasfilename(defaultextension='.JPEG')
    img_1.save(img2)
    messagebox.showinfo("congrats", "Converted to JPG")

def convert3():
    global img_1
    img3=filedialog.asksaveasfilename(defaultextension='.WEBp')
    img_1.save(img3)
    messagebox.showinfo("congrats", "Converted to WEBp")

label=Label(root,text="Choose the file to convert",bg="lightblue",font=("Roman",15))
label.pack(padx=10,pady=10)
entry=Entry(root,width=35)#.place(x=100,y=50)
entry.pack(padx=25,pady=15,anchor='ne')

button=Button(root,text="browse",padx=35,pady=7,command=Choose_file,bg="orange").place(x=20,y=50)
button=Button(root,text="Convert to PNG",padx=35,pady=20,command=convert1,bg="#008080").place(x=220,y=100)
button=Button(root,text="Convert to JPEG",padx=35,pady=20,command=convert2,bg="#008080").place(x=20,y=100)
button=Button(root,text="Convert to WEBp",padx=35,pady=20,command=convert3,bg="#008080").place(x=100,y=180)


root.config(bg="lightblue")
root.deiconify()
root.mainloop()
    