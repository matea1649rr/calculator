from tkinter import *


window=Tk()
window.geometry("300x400")
window.title("CALCULATOR")

bar = Entry(window,width=22,font=("Ubuntu",18,"normal"),fg="blue",bg="Pale Turquoise")
bar.place(x=5,y=3)

X = 75
Y = 75
 
def insert(num):
    bar['fg']="blue"
    text = bar.get()
    if (text.split() == []) and (num=="/" or num=="*" or num==")"):
        num = '' 
    elif (text.endswith('/')) and (num=="+" or num=="-" or num=="/" or num=="*"):
        num = ''
    elif (text.endswith('+')) and (num=="+" or num=="-" or num=="/" or num=="*"):
        num = ''
    elif (text.endswith('-')) and (num=="+" or num=="-" or num=="/" or num=="*"):
        num = ''

    elif (text.endswith('.')) and (num=="." or num=="+" or num=="-" or num=="/" or num=="*"):
        num=''

    
     
    bar.insert(END,num)

def BackSpace():
    bar['fg']="blue"
    try:
        text = bar.get()
        l = list(text)
        l.pop()
        Text = ""
        for i in range(len(l)):
            Text += l[i]
        bar.delete(0,END)
        bar.insert(0,Text)
    except:
        None
        
def Delete():
    bar['fg']="blue"
    bar.delete(0,END)

def BracketCheck():
    text = str(bar.get())
    Text = list(text)
    a=0
    for i in range(len(Text)):
        if Text[i] == "(":
            a+=1
    b=0
    for i in range(len(Text)):
        if Text[i] == ")":
            b+=1
    Add = a-b
    return Add

def Answer():
    text = str(bar.get())

    Add = BracketCheck()
    if Add>0:
        bar.insert(END,Add*")")
    
    else:
        try:
            answer = eval(text)
            Delete()
            bar.insert(0,answer)
            bar['fg'] = "forestgreen"
        except:
            bar[' fg'] = "red"


n1 = Button(window,text="1",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="lightSkyBlue",command=lambda:insert("1"))
n1.place(x=0,y=Y+20)

n2 = Button(window,text="2",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="lightSkyBlue",command=lambda:insert("2"))
n2.place(x=X,y=Y+20)

n3 = Button(window,text="3",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="lightSkyBlue",command=lambda:insert("3"))
n3.place(x=2*X,y=Y+20)

n4 = Button(window,text="4",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="lightSkyBlue",command=lambda:insert("4"))
n4.place(x=0,y=(2*Y)+20)

n5 = Button(window,text="5",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="lightSkyBlue",command=lambda:insert("5"))
n5.place(x=X,y=(2*Y)+20)

n6 = Button(window,text="6",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="lightSkyBlue",command=lambda:insert("6"))
n6.place(x=2*X,y=(2*Y)+20)

n7 = Button(window,text="7",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="lightSkyBlue",command=lambda:insert("7"))
n7.place(x=0,y=(3*Y)+20)

n8 = Button(window,text="8",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="lightSkyBlue",command=lambda:insert("8"))
n8.place(x=X,y=(3*Y)+20)

n9 = Button(window,text="9",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="lightSkyBlue",command=lambda:insert("9"))
n9.place(x=2*X,y=(3*Y)+20)

n0 = Button(window,text="0",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="lightSkyBlue",command=lambda:insert("0"))
n0.place(x=X,y=(4*Y)+20)



dot = Button(window,text=".",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="moccasin",command=lambda:insert("."))
dot.place(x=0,y=(4*Y)+20)

equal = Button(window,text="=",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="moccasin",command=Answer)
equal.place(x=2*X,y=(4*Y)+20)

####################################################################################################

mult = Button(window,text="X",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="paleGreen",command=lambda:insert("*"))
mult.place(x=3*X,y=Y+20)

div = Button(window,text="/",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="paleGreen",command=lambda:insert("/"))
div.place(x=3*X,y=(2*Y)+20)

plus = Button(window,text="+",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="paleGreen",command=lambda:insert("+"))
plus.place(x=3*X,y=(3*Y)+20)

minus = Button(window,text="-",font=("Courier New",16,"bold"),padx = 20,pady = 16,bd = 4,bg="paleGreen",command=lambda:insert("-"))
minus.place(x=3*X,y=(4*Y)+20)



AC = Button(window,text="AC",font=("Courier New",16,"bold"),padx = 14,pady = 6,bd = 4,bg="navajoWhite",command=Delete)
AC.place(x=0,y=Y-35)

back = Button(window,text=u"\u2190",font=("Courier New",16,"bold"),padx = 20,pady = 6,bd = 4,bg="navajoWhite",command=BackSpace)
back.place(x=X,y=Y-35)

Open = Button(window,text="(",font=("Courier New",16,"bold"),padx = 20,pady = 6,bd = 4,bg="navajoWhite",command=lambda:insert("("))
Open.place(x=2*X,y=Y-35)

Close = Button(window,text=")",font=("Courier New",16,"bold"),padx = 20,pady = 6,bd = 4,bg="navajoWhite",command=lambda:insert(")"))
Close.place(x=3*X,y=Y-35)



window.mainloop()