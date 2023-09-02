from tkinter import*
import customtkinter

root=Tk()
root.title("Acronym Generator")

label1=Label(root,text="Enter your phrase: ", bg="Grey")
label1.grid(pady=0,column=0,row=1)

user=customtkinter.CTkEntry(root,width=200) 
user.grid(column=1,row=1,padx=20,pady=30)

label2=Label(root,text="Your acronym: ",bg="Grey")
label2.grid(pady=0,column=0,row=3)

ab=customtkinter.CTkEntry(root, width=200)
ab.grid(column=1,row=3)

def acronym_gentrator():
    input_string=user.get()
    text=input_string.split(" ")
    acronym=" "
    for i in text:
        if i:
            acronym += i[0].upper()
    ab.delete(0,END)
    ab.insert(0,acronym)
    
Button1=customtkinter.CTkButton(root,text="Generate Acronym",command=lambda:acronym_gentrator())
Button1.grid(column=1,row=2,columnspan=2)

root.config(bg="Grey")
root.mainloop()
