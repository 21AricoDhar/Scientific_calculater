
from tkinter import *
import math

def click(value):

    ex=entryfield.get()
    answer=""

    try:

        if value=="C":
            ex=ex[0:len(ex)-1]
            entryfield.delete(0,END)
            entryfield.insert(0,ex)
            return

        elif value=="CE":
            entryfield.delete(0,END) 
        
        elif value=="SQRT":
            answer=math.sqrt(eval(ex))

        elif value=="pi":
            answer=math.pi

        elif value=="cose":
            answer=math.cos(math.radians(eval(ex)))

        elif value=="sin":
            answer=math.sin(math.radians(eval(ex)))

        elif value=="tan":
            answer=math.tan(math.radians(eval(ex)))

        elif value=="2pi":
            answer=2*math.pi

        elif value=="cosh":
            answer=math.cosh(eval(ex))

        elif value=="sinh":
            answer=math.sinh(eval(ex))

        elif value=="tanh":
            answer=math.tanh(eval(ex))

        elif value==chr(8731):
            answer=eval(ex)**(1/3)

        elif value=="x\u02b8":
            entryfield.insert(END,"**")
            return

        elif value=="x\u00B3":
            answer=eval(ex)**3

        elif value=="x\u00B2":
            answer=eval(ex)**2

        elif value=="ln":
            answer=math.log2(eval(ex))

        elif value=="deg":
            answer=math.degrees(eval(ex))

        elif value=="rad":
            answer=math.radians(eval(ex))

        elif value=="e":
            answer=math.e

        elif value=="log10":
            answer=math.log10(eval(ex))

        elif value=="x!":
            answer=math.factorial(ex)

        elif value==chr(247):
            entryfield.insert(END, "/")
            return

        elif value=="=":
            answer=eval(ex)

        else:
            entryfield.insert(END,value)
            return

        entryfield.delete(0,END)
        entryfield.insert(0,answer)
    except SyntaxError:
        pass



root=Tk()
root.title("Scientific Calculator")
root.configure(bg="grey")
# width , height ,distance from x-axis , distance from y-axis
root.geometry("680x486+100+100")

entryfield=Entry(root,font=("arial",20,"bold"),bg="silver",fg="black",bd=10,relief=SUNKEN,width=30)
entryfield.grid(row=0,column=0,columnspan=8)

button_text_list=["C","CE","SQRT","+","pi","cose","sine","tan",
                  "1", "2", "3", "-","2pi","cosh","sinh","tanh",
                  "4", "5", "6", "*",chr(8731),"x\u02b8","x\u00B3","x\u00B2",
                  "7", "8", "9", chr(247),"ln","deg","rad","e",
                  "0",".","%","=","log10","(", ")","x!"]
            
rowvalue=1
columnvalue=0

for i in button_text_list:

    button=Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg="grey",fg="black",font=("arial",18,"bold"),
        activebackground="red",command=lambda button=i:click(button))
    button.grid(row=rowvalue,column=columnvalue,pady=1)
    columnvalue+=1
    if columnvalue>7:
        rowvalue+=1
        columnvalue=0



root.mainloop()
