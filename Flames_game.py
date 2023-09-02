from tkinter import*
from tkinter.messagebox import showinfo,showerror

root=Tk()
root.title("Flames")
root.geometry("350x270")
root.resizable(False,False)
root.config(bg="peach puff")


def match_char_remover(list1,list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                c=list2[j]

                list1.remove(c)
                list2.remove(c)

                list3=list1+['*']+list2

                return [list3,True]
    
    list3=list1+['*']+list2
    return [list3,False]


def rock():
    if __name__=="__main__":
     player1=Player1.get()
     player1.lower()
     player1.replace(" ", '')
     player1_list=list(player1)

     player2=Player2.get()
     player2.lower()
     player2.replace(" ", '')
     player2_list=list(player2)

     proceed=True
    try:
        if player1=="":
            showerror(title="Error",message="Please enter the first name!!")
        elif player2=="":
            showerror(title="Error",message="please enter the second name")
        else:
            while proceed:
                rtn_match_list=match_char_remover(player1_list, player2_list)

                con_list=rtn_match_list[0]

                proceed=rtn_match_list[1]

                star_list=con_list.index("*")

                player1_list=con_list[:star_list]
                player2_list=con_list[star_list+1:]

            count=len(player1_list)+len(player2_list)

            result=['Friends','love','Affection','marriage','Enemy','Siblings']

            while len(result)>1:

                index_split=(count % len(result)-1)

                if index_split >=0:
                    right=result[index_split+1:]
                    left=result[:index_split]

                    result=right+left
                
                else:
                    result=result[:len(result)-1]

            showinfo(title="Flames",message="Relationship status: "+result[0])
    except :
        showerror(title="Error",message="please review your code and debugg...!!")

Player1=StringVar()
Player2=StringVar()

head_label=Label(root,text="FLAMES!!!",fg="RED",padx=9,pady=8,bg="peach puff",font='stencil 17').place(x=150,y=20)

p1_label=Label(root,text='Player1:',font="Arial 15",bg="yellow")
p1_label.place(x=70,y=65)

p2_label=Label(root,text='Player2:',font="Arial 15",bg="yellow")
p2_label.place(x=70,y=115)

pl1_entry=Entry(root,textvariable=Player1,width=26,)
pl1_entry.place(x=150,y=65)
pl2_entry=Entry(root,textvariable=Player2,width=26)
pl2_entry.place(x=150,y=115)


ROCK=Button(root,text="Rock!!",command=rock,padx=45,pady=20,bg="salmon")
ROCK.place(x=130,y=170)
root.mainloop()