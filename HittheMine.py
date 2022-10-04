from tkinter import *
from random import *
from time import *
import os

def new_game():
    label['text']="Start!"
    button_placer()
    mine_placer()

def exit():
    file =open("score.txt",'w')
    file.write()
    window.destroy

def highest_score():
    if os.path.isfile("score.txt") :
        file= open("score.txt",'r')
        text = file.read()
        score =text.split(" ")
        time=score[1]
    else:
        time="0"
    return time

def About():
    pass
def flag_mine(i,j):
    global buttons
    global bomb
    if bomb < 5 :
        buttons[i][j].config(bg='red')
    else :
        label['text']="You lose"
    bomb+=1
    

def win_chechker():

    file =open("score.txt",'r')
    text = file.read()
    if text ==" ":
        time=0
    else:
        score =text.split(" ")
        time=int(score[1])
    file.close()
    file = open("score.txt",'w')
    time2=localtime()
    scorep=str(time2.tm_min-time1.tm_min)+"."+str(time2.tm_sec-time1.tm_sec)
    print(scorep,time)
    if time > float(scorep) :
           file.write("Davut "+scorep)
    file.close()

#Starting block   

window= Tk()
window.title("\t\t\tHIT THE MINE")
window.geometry("550x650")
menubar = Menu(window)
window.config(menu=menubar)
gamemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Options",menu=gamemenu)
gamemenu.add_command(label="New Game",command=new_game,compound="left")
gamemenu.add_command(label="About Game",command=About,compound="left")
gamemenu.add_command(label="Exit",command=exit,compound="left")
bomb=0
label = Label(window,text="Start!",
                    font=('Arial',10,'bold'),
                      fg='#00FF00',
                      bg='black',
                      relief=RAISED,
                      bd=10,
                      )

score_label = Label(window,text="Best Time ="+highest_score(),
                    font=('Arial',10,'bold'),
                      fg='orange',
                      bg='black',
                      relief=RAISED,
                      bd=10,
                    )   

frame = Frame(window,relief=RAISED)

buttons =  [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
matrix = buttons #extra field for controlling the background

def controller(row,column):
    
    x=0
    if matrix[row][column]=="11":
        label['text']="You Lose"
    if row <9: 
        if matrix[row+1][column]=="11":
            x+=1
            buttons[row][column]['text']=str(x)
    if row>0:
        if matrix[row-1][column]=="11":
            x+=1
            buttons[row][column]['text']=str(x)
    if column<9:
        if matrix[row][column+1]=="11":
            x+=1
            buttons[row][column]['text']=str(x)
    if column>0:       
        if matrix[row][column-1]=="11":
            x+=1
            buttons[row][column]['text']=str(x)
    if x == 0 and matrix[row][column] != "11":
        buttons[row][column].config(relief=SUNKEN)
        buttons[row+1][column].config(relief=SUNKEN)
        buttons[row-1][column].config(relief=SUNKEN)
        buttons[row][column+1].config(relief=SUNKEN)
        buttons[row][column-1].config(relief=SUNKEN)
        

def button_placer():  
    for i in range(10):
        for j in range(10):
            buttons[i][j] = Button(frame,text="",height=3,bg='gray', width=6,command=lambda i=i,j=j:controller(i,j))
            buttons[i][j].bind("<Button-3>",lambda e, i=i,j=j :flag_mine(i,j))
            buttons[i][j].grid(row=i,column=j)

def mine_placer():
    for i in range(5):
        x = randint(0,9)
        y = randint(0,9)
        if matrix[x][y]!="11": # for preventing override
            matrix[x][y]="11" 
        else:
            i-=1

global time1 #for calculating the time for recording score
time1 = localtime()
new_game()


score_label.place(x=50,y=0)  
label.pack(side=TOP)
frame.pack(side=BOTTOM)
window.mainloop()
