from tkinter import*
#from PIL import ImageTk ,Image
import math

root=Tk()
root.title("Simple Calculator")


def Validate_entry(text):
    if text.isdigit:
        return True
    elif text=="":
        return True
    else:
        return False

# entry column
e=Entry(root,width=35,borderwidth=5,validate="key",validatecommand=lambda:(root.register(Validate_entry),'%S'))
e.grid(row=0,column=0,columnspan=3,padx=20,pady=30)
#c=Canvas(root,width=80,height=80,bg='white')
#c.grid()


#define the number button click function
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
#define clear button function
def button_clear():
    e.delete(0,END)
#define add button function
def button_add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0,END)
#define equal button function
def button_equal():
    second_number=e.get()
    e.delete(0,END)

    if math =="addition":
        e.insert(0,f_num+int(second_number))
    elif math=="subtraction":
        e.insert(0,f_num-int(second_number))
    elif math=="multiplication":
        e.insert(0,f_num*int(second_number)) # type: ignore
    elif math =="division":
        e.insert(0,f_num/int(second_number)) # type: ignore

#define substraction function
def button_minus():
    first_number=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first_number)
    e.delete(0,END)
#define multiplication function
def button_multiply():
    first_number=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_number)
    e.delete(0,END)
#define divide functin
def button_divide():
    first_number=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_number)
    e.delete(0,END)
#define Square Root function
def button_SquareRoot():
    first_number=e.get()
    global f_num
    global math_op
    math_op="SquareRoot"
    f_num=int(first_number)
    result_sqrt=(f_num**0.5,2)
    e.delete(0,END)
    e.insert(0,result_sqrt)
#define logarithem function
def button_lothm():
    first_number=e.get()
    global f_num
    f_num=float(first_number)
    result_log=math.log(f_num,10)
    e.delete(0,END)
    e.insert(0,result_log) # type: ignore

#define button
button1=Button(root,text="1",font=("ZapfDingbats",9,"bold"),padx=40,pady=20,command=lambda:button_click(1),bg="#7FFFD4")
button2=Button(root,text="2",font=("ZapfDingbats",9,"bold"),padx=40,pady=20,command=lambda:button_click(2),bg="#4682B4")
button3=Button(root,text="3",font=("ZapfDingbats",9,"bold"),padx=40,pady=20,command=lambda:button_click(3),bg="#1E90FF")
button4=Button(root,text="4",font=("ZapfDingbats",9,"bold"),padx=40,pady=20,command=lambda:button_click(4),bg="#7FFFD4")
button5=Button(root,text="5",font=("ZapfDingbats",9,"bold"),padx=40,pady=20,command=lambda:button_click(5),bg="#4682B4")
button6=Button(root,text="6",font=("ZapfDingbats",9,"bold"),padx=40,pady=20,command=lambda:button_click(6),bg="#1E90FF")
button7=Button(root,text="7",font=("ZapfDingbats",9,"bold"),padx=40,pady=20,command=lambda:button_click(7),bg="#7FFFD4")
button8=Button(root,text="8",font=("ZapfDingbats",9,"bold"),padx=40,pady=20,command=lambda:button_click(8),bg="#4682B4")
button9=Button(root,text="9",font=("ZapfDingbats",9,"bold"),padx=40,pady=20,command=lambda:button_click(9),bg="#1E90FF")
button0=Button(root,text="0",font=("ZapfDingbats",9,"bold"),padx=39,pady=20,command=lambda:button_click(0),bg="#008080")
buttonclear=Button(root,text="Clear",font=("ZapfDingbats",9,"bold"),padx=79,pady=20,command=button_clear,bg="#7B68EE")
buttonadd=Button(root,text="+",font=("ZapfDingbats",9,"bold"),padx=38,pady=20,command=button_add,bg="#DDA0DD")
buttonequal=Button(root,text="=",font=("ZapfDingbats",9,"bold"),padx=89.5,pady=20,command=button_equal,bg="#7B68EE")
buttonminus=Button(root,text="-",font=("ZapfDingbats",9,"bold"),padx=40,pady=20,command=button_minus,bg="#DDA0DD")
buttonmultiply=Button(root,text="X",font=("ZapfDingbats",9,"bold"),padx=40.5,pady=20,command=button_multiply,bg="#DDA0DD")
buttondivide=Button(root,text="/",font=("ZapfDingbats",9,"bold"),padx=42,pady=20,command=button_divide,bg="#DDA0DD")
button_root=Button(root,text="√",font=("ZapfDingbats",9,"bold"),padx=38.3,pady=20,command=lambda:button_SquareRoot(),bg="#663399")
button_log=Button(root,text="log",font=("ZapfDingbats",9,"bold"),padx=37,pady=20,command=lambda:button_lothm(),bg="#663399")


#put button on screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonadd.grid(row=5,column=0)
buttonequal.grid(row=5,column=1,columnspan=2)
buttonclear.grid(row=4,column=1,columnspan=2)

buttonminus.grid(row=6,column=0)
buttonmultiply.grid(row=6,column=1)
buttondivide.grid(row=6,column=2)

button_root.grid(row=7,column=0)
button_log.grid(row=7,column=1)
#image=PhotoImage(file="H:\\my library\\41aOggNg3YS.jpg")
#img=ImageTk.PhotoImage(Image.open("41aOggNg3YS.jpg"))
root.config(bg="#8585c2")
root.mainloop()