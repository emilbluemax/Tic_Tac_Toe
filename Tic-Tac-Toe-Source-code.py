from tkinter import*
from tkinter import messagebox

window=Tk()
window.title('TIC TAC TOE')
window.geometry('700x400')
lbl=Label(window,text="TIC TAC TOE",font=('times',15))
lbl.grid(column=3, row=0)

x = Label(window,text='Please ENTER NAMES to continue !!')
x.grid(row=1,column=3)

def enable():
    if (pl1.get().isalnum() and pl2.get().isalnum()):
        b1['state']='normal'
        b2['state']='normal'
        b3['state']='normal'
        b4['state']='normal'
        b5['state']='normal'
        b6['state']='normal'
        b7['state']='normal'
        b8['state']='normal'
        b9['state']='normal'
    

def accept1():
    mssg = pl1.get()+"'s token is : X"
    lb4 = Label(window,text=mssg)
    lb4.grid(row=3,column=0)
    pl1['state'] ='disabled'
    enable()

def accept2():
    mssg = pl2.get()+"'s token is : O"
    lb4 = Label(window,text=mssg)
    lb4.grid(row=5,column=0)
    pl2['state'] ='disabled'
    enable()

winner = False
flag = 1
def check():
    global winner
    global flag
    flag+=1
    btn1 = b1['text']
    btn2 = b2['text']
    btn3 = b3['text']
    btn4 = b4['text']
    btn5 = b5['text']
    btn6 = b6['text']
    btn7 = b7['text']
    btn8 = b8['text']
    btn9 = b9['text']
    if((btn1==btn2==btn3=='X')or(btn1==btn2==btn3=='O')):
        win(btn1)
    if((btn4==btn5==btn6=='X')or(btn4==btn5==btn6=='O')):
        win(btn4)
    if((btn7==btn8==btn9=='X')or(btn7==btn8==btn9=='O')):
        win(btn7)
    if((btn1==btn4==btn7=='X')or(btn1==btn4==btn7=='O')):
        win(btn1)
    if((btn5==btn2==btn8=='X')or(btn5==btn2==btn8=='O')):
        win(btn5)
    if((btn9==btn6==btn3=='X')or(btn9==btn6==btn3=='O')):
        win(btn9)
    if((btn1==btn5==btn9=='X')or(btn1==btn5==btn9=='O')):
        win(btn1)
    if((btn7==btn5==btn3=='X')or(btn7==btn5==btn3=='O')):
        win(btn7)
    if (flag == 10 and winner == False):
        messagebox.showinfo("RESULT","The game has been TIED !!!")
        window.destroy()

def win(y):
    global winner
    winner = True
    if y == 'X':
        b = "RESULT"
        a = " CONGRATULATIONS !!! Player 1 :"+pl1.get().upper()+" has WON the game !! "
        messagebox.showinfo(b,a)
        window.destroy()
    else:
        c = "RESULT"
        d = " CONGRATULATIONS !!! Player 2 :"+pl2.get().upper()+" has WON the game !! "
        messagebox.showinfo(c,d)
        window.destroy()
    
x=0
def display1():
    global x
    if x%2==0:
        b1['text']='X'
        b1['bg']='white'
    elif x%2!=0:
        b1['text']='O'
        b1['bg']='yellow'
    x+=1
    b1['state']='disabled'
    check()
    
def display2():
    global x
    if x%2==0:
        b2['text']='X'
        b2['bg']='white'
    elif x%2!=0:
        b2['text']='O'
        b2['bg']='yellow'
    x+=1
    b2['state']='disabled'
    check()
    
def display3():
    global x
    if x%2==0:
        b3['text']='X'
        b3['bg']='white'
    elif x%2!=0:
        b3['text']='O'
        b3['bg']='yellow'
    x+=1
    b3['state']='disabled'
    check()
    
def display4():
    global x
    if x%2==0:
        b4['text']='X'
        b4['bg']='white'
    elif x%2!=0:
        b4['text']='O'
        b4['bg']='yellow'
    x+=1
    b4['state']='disabled'
    check()
    
def display5():
    global x
    if x%2==0:
        b5['text']='X'
        b5['bg']='white'
    elif x%2!=0:
        b5['text']='O'
        b5['bg']='yellow'
    x+=1
    b5['state']='disabled'
    check()
    
def display6():
    global x
    if x%2==0:
        b6['text']='X'
        b6['bg']='white'
    elif x%2!=0:
        b6['text']='O'
        b6['bg']='yellow'
    x+=1
    b6['state']='disabled'
    check()
    
def display7():
    global x
    if x%2==0:
        b7['text']='X'
        b7['bg']='white'
    elif x%2!=0:
        b7['text']='O'
        b7['bg']='yellow'
    x+=1
    b7['state']='disabled'
    check()
    
def display8():
    global x
    if x%2==0:
        b8['text']='X'
        b8['bg']='white'
    elif x%2!=0:
        b8['text']='O'
        b8['bg']='yellow'
    x+=1
    b8['state']='disabled'
    check()
    
def display9():
    global x
    if x%2==0:
        b9['text']='X'
        b9['bg']='white'
    elif x%2!=0:
        b9['text']='O'
        b9['bg']='yellow'
    x+=1
    b9['state']='disabled'
    check()

b1=Button(window,text = "", command=display1,bg='cyan',fg="black",width="6",height="3",font=("Times", "15"),state='disabled',borderwidth=5)
b1.grid(column=5,row=2)                                                    
b2=Button(window,text = "", command=display2,bg="cyan",fg="black",width="6",height="3",font=("Times", "15"),state='disabled',borderwidth=5)
b2.grid(column=6,row=2)
b3=Button(window,text = "", command=display3,bg="cyan",fg="black",width="6",height="3",font=("Times", "15"),state='disabled',borderwidth=5)
b3.grid(column=7,row=2)
b4=Button(window,text = "", command=display4,bg="cyan",fg="black",width="6",height="3",font=("Times", "15"),state='disabled',borderwidth=5)
b4.grid(column=5,row=3)
b5=Button(window,text = "", command=display5,bg="cyan",fg="black",width="6",height="3",font=("Times", "15"),state='disabled',borderwidth=5)
b5.grid(column=6,row=3)
b6=Button(window,text = "", command=display6,bg="cyan",fg="black",width="6",height="3",font=("Times", "15"),state='disabled',borderwidth=5)
b6.grid(column=7,row=3)
b7=Button(window,text = "", command=display7,bg="cyan",fg="black",width="6",height="3",font=("Times", "15"),state='disabled',borderwidth=5)
b7.grid(column=5,row=4)
b8=Button(window,text = "", command=display8,bg="cyan",fg="black",width="6",height="3",font=("Times", "15"),state='disabled',borderwidth=5)
b8.grid(column=6,row=4)
b9=Button(window,text = "", command=display9,bg="cyan",fg="black",width="6",height="3",font=("Times", "15"),state='disabled',borderwidth=5)
b9.grid(column=7,row=4)

player1 = Label(window,text='Player 1 : ')
player1.grid(row=2,column=0)
pl1 = Entry(window,bg='white',fg='black',width=15)
pl1.grid(row=2,column=1)
pl1b = Button(window,text="Enter",command=accept1)
pl1b.grid(row=2,column=2)

player2 = Label(window,text='Player 2 : ')
player2.grid(row=4,column=0)
pl2 = Entry(window,bg='white',fg='black',width=15)
pl2.grid(row=4,column=1)
pl2b = Button(window,text="Enter",command=accept2)
pl2b.grid(row=4,column=2)

window.mainloop()
