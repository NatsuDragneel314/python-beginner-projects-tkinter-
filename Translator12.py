from translate import Translator
from tkinter import*
from tkinter.messagebox import showerror,showinfo
#import messagebox
import customtkinter

root=Tk()
root.title("Translator")
root.geometry("500x260")
root.resizable(False,False)

input_translation=StringVar()
output_translation=StringVar()
entry1=customtkinter.CTkEntry(root,textvariable=input_translation,width=200).place(x=210,y=40)
entry2=customtkinter.CTkEntry(root,width=200,textvariable=output_translation)
entry2.place(x=210,y=120)

label1=customtkinter.CTkLabel(root,text="What you want to translate: ")
label1.place(x=40,y=40)

label2=customtkinter.CTkLabel(root,text="Select The Lang to which \n you want to translate:").place(x=40,y=80)

def translate():
    e=input_translation.get()
    translator= Translator(to_lang=language1.get())
    translation= translator.translate(e)
    #showinfo(title="Translation",message=f"Your Translation is : {translation}")
    entry2.delete(0,END)
    entry2.insert(0, translation)


language1=StringVar(root)
language1.set("hi")
language_menu=OptionMenu(root,language1, "ml","mr","ja","hi",)
language_menu.config(width=7,font=('Cartoon',12))
language_menu.place(x=210,y=80)


Tbutton=customtkinter.CTkButton(root,text="Translate",command=lambda:translate(),fg_color="purple").place(x=210,y=180)


root.config(background="peach puff")
root.mainloop()