import datetime
from tkinter import*
import customtkinter
import time
import winsound
from tkinter import messagebox
import threading

clock=Tk()
clock.title("My Alarm Clock")
clock.geometry("458x210")

image=PhotoImage(file="H:\\my library\\projects\\Alarm_clock1.py\\alrm.png")
canvas1=Canvas(clock,width=1000,height=1000)
canvas1.create_image(0,1,image=image,anchor="nw")
canvas1.pack()

canvas1.create_text(150,50,text ="                         Hour:           Min:           Sec:",font=("Arial",15,),fill="#39FF14")
canvas1.create_text(150,200,text="Please Use 24 Hours Formate!!!",font=("Comic Sans MS",15),fill="#39FF14")


def alarm(set_ur_alarm):
    while True:
        time.sleep(1)
        set_ur_alarm= f"{Hours.get()}:{minutes.get()}:{seconds.get()}"
        current_time=datetime.datetime.now()
        now=current_time.strftime("%H:%M:%S")
        date=current_time.strftime("%d/%m/%Y")
        print("Current date is :",date)
        print(now)
        if now == set_ur_alarm:
            #print("Time To wake up!!!")
            winsound.PlaySound('H:\my library\projects\Alarm_clock1.py\ww.wav', winsound.SND_ASYNC)
            messagebox.showinfo("Time TO wake Up!!!")
            break

Hours=StringVar()
minutes=StringVar()
seconds=StringVar()


def actual_time():
    set_ur_alarm=f"{Hours.get()}:{minutes.get()}:{seconds.get()}"
    alarm(set_ur_alarm)

def Validate_entry(text):
    if text.isdigit():
        return True
    elif text=="":
        return True
    else:
        return False


def setthread():
    t1=threading.Thread(target=actual_time)
    t1.start()

HoursTime=customtkinter.CTkEntry(clock,textvariable=Hours,width=70,validate="key",validatecommand=(clock.register(Validate_entry),'%S'),bg_color="#4B0082")#.place(x=100,y=30)
minuteTime=customtkinter.CTkEntry(clock,textvariable=minutes,width=70,validate="key",validatecommand=(clock.register(Validate_entry),'%S'),bg_color="#4B0082")#.place(x=200,y=30)
secondsTime=customtkinter.CTkEntry(clock,textvariable=seconds,width=70,validate="key",validatecommand=(clock.register(Validate_entry),'%S'),bg_color="#4B0082")#.place(x=300,y=30)

HourTime_windows=canvas1.create_window(100,70,anchor="nw",window=HoursTime)
minuteTime_windows=canvas1.create_window(200,70,anchor="nw",window=minuteTime)
secondsTime_windows=canvas1.create_window(300,70,anchor="nw",window=secondsTime)



button=customtkinter.CTkButton(clock,text="Set your alarm",command=setthread,corner_radius=0,fg_color=("purple"))#.place(x=160,y=90)
button_window=canvas1.create_window(170,120,anchor="nw",window=button)


customtkinter.set_appearance_mode("Dark")
clock.mainloop()