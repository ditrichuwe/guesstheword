import tkinter as tk
import random
import tkinter.messagebox as mb

words=["laptop","school","googles"]
randomword=random.choice(words)

#letters that we print
letters=[]

attempts=5

def restart():
    global randomword,attempts
    randomword=random.choice(words)
    showstars()
    attempts=5
    letters.clear()

def attemptsdecrease(letter):
    global attempts
    if letter not in randomword:
        attempts=attempts-1
        labelattempts["text"]=f"Attempts:{attempts}"
    if attempts==0:
        labelattempts["text"]="you lost"
        mb.showinfo("Information over the game","You lost")
        restart()
        labelattempts["text"]=f"Attempts:{attempts}"

def showstars():
    stars=""
    for letter in randomword:
        stars+="*"
    labeltext["text"]=stars

def checkwin(answer):
    if randomword==answer:
        mb.showinfo("Information over the game","You win")
        restart()
        labelattempts["text"]=f"Attempts:{attempts}"



def check():
    letter=textnum1.get()
    letters.append(letter)
    result=""
    for sign in randomword:
        if sign in letters:
            result+=sign
        else:
            result+="*"
    labeltext["text"]=result
    textnum1.delete(0,"end")
    attemptsdecrease(letter)
    checkwin(result)



window=tk.Tk()
window.title("Notes")
window.geometry("400x400")


textnum1=tk.Entry(window,width=25)
textnum1.place(x=80,y=90)
textnum1.focus()

labeltext=tk.Label(window,text="hello",font=("Arial",20))
labeltext.place(x=120,y=35)

labelattempts=tk.Label(window,text=f"Attempts:{attempts}")
labelattempts.place(x=120,y=20)

#button
button1=tk.Button(window,text="Check",command=check)
button1.place(x=120,y=130)





































































showstars()
window.mainloop()