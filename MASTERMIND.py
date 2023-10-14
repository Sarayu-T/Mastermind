from tkinter import *
from tkinter import messagebox
import time, random
from playsound import playsound
class MASTERMINDS():
    #INITIALISING THE VARIABLES OF CLASS MASTERMIND
    def __init__(self):
        self.h = 0    # h for horizontal arrangement of buttons
        self.v = 0    # v for vertical arrangement of buttons
        self.xcoord = 150  # xcoord for buttons
        self.ycoord = 160   # ycoord for buttons
        self.pallette = ["red","green","yellow","white","violet","orange"]
        self.code = random.choices(self.pallette, k=4)    # Generates the colour code
        self.guess = []
        self.buttons=[['None']*4 for _ in range(10)]
        #self.c = 0    # c for correct colour
        self.p = 0    # p for correct position
        
        self.root = Tk()           # Instances in the Parent 'root' window
        self.main_window()
        self.frames()
        self.placing()
        self.guesses()
        self.placing_buttons()
        self.root.mainloop()  
    # MAIN WINDOW DETAILS
    def main_window(self):
        self.root.geometry("840x900")
        self.root.title("MASTERMIND GAME")
        self.root.config(bg="#E7F2F8")
        print(self.code)     # Remove later

    # EXIT BUTTON
    def exit(self):   
        self.res = messagebox.askyesno("MASTERMIND","Leaving so soon?")
        if self.res == True:
            messagebox.showinfo("MASTERMIND", "Killing the window in 5 seconds")
            time.sleep(5)
            self.root.destroy()
        elif self.res == False:
            pass
        else:
            messagebox.showerror('error', 'something went wrong!')

    # Welcome Message Frame, Rules & Packing
    def frames(self):
        w_frame = Frame(self.root,bg="#E7F2F8", highlightbackground="green")
        w_frame.pack(fill="x")
        Welcome = Label(w_frame, text="Welcome to MASTERMIND!", bg="#E7F2F8" ,font="Helvetica 23 bold", pady=15)
        Welcome.pack()
        Rule = Label(w_frame, text="Guess the 4-colour code!! \n You get to chooose from Red(R), Blue(B), Green(G), Yellow(Y), White(W), Violet(V), Orange(O)", font="merriwether 10",bg="#E7F2F8")
        Rule.pack()
        tries = Label(w_frame, text="You have 10 tries!", bg = "#E7F2F8", font="merriwether 10 bold" )
        tries.pack()


    # Guesses & Packing
    def guesses(self):

        Guess = Label(self.root, text="Your guesses: ", font="merriwether 9 underline",bg="#E7F2F8")
        Guess.place(x=160,y=135)
    
    # Creating frame for Placing Buttons & Packing
    def placing(self):
        self.b_frame = Frame(self.root, bg="#74BDCB",borderwidth=18)
        self.b_frame.pack(side=LEFT,fill="y")

    # Creating the colour buttons & Packing "R", "B", "G", "Y","W", "V", "P"
    def placing_buttons(self):
        def check():
            if len(self.guess)<4:
                messagebox.showwarning("ALERT!", "4 buttons must be chosen")
                self.v-=1
                self.lis=[i for i in self.buttons[self.v] if i!='None']

                for j in self.lis:
                    j.place_forget()
                self.guess=[]
                self.h=0
                for i in self.buttons[self.v]:
                    i='None'

            else:
                for i in range(0,4):
                    if self.code[i]==self.guess[i]:
                        self.p+=1
                self.guess = []
                if self.p==4:
                    playsound("cheering.mp3")
                    messagebox.showinfo(":))", "HURRAH!! YOU'VE WON")
                    self.root.quit()
            
                else:
                    Label(self.root,text=str(self.p)+" positions correct").place(x=self.xcoord+50,y=self.ycoord)
                    self.p=0
                    if self.v>=10:
                        self.show = Tk()        # shows the code after 10 guesses in a new window
                        self.show.geometry("300x300")
                        Label(self.show, text="The code was: ", font="merriwether 10 bold").place(x=10,y=10)   # added the label

                        for i in range(0,4):
                            Button(self.show,bg=self.code[i],padx=15,pady=4).place(x=(30+(50*i)),y=40)


                        red["state"]=DISABLED
                        blue["state"]=DISABLED
                        green["state"]=DISABLED
                        yellow["state"]=DISABLED
                        white["state"]=DISABLED
                        violet["state"]=DISABLED
                        orange["state"]=DISABLED
                        sub["state"]=DISABLED
                        clearb["state"]=DISABLED
                        self.root.quit()
                        self.show.mainloop()
        self.h=0
        

        def button_click(str1):
            try:
                self.xcoord=(self.h*50)+160
                self.ycoord=(self.v*50)+160
                self.guess.append(str1)
                self.buttons[self.v][self.h]=Button(self.root,bg=str1,padx=15,pady=4)
                self.buttons[self.v][self.h].place(x=self.xcoord,y=self.ycoord)
                self.h+=1

            except:
                messagebox.showwarning("ALERT!", "you can only choose 4 buttons,silly")
                self.lis=[i for i in self.buttons[self.v]]
                for j in self.lis:
                    j.destroy()
                self.guess=[]
                self.h=0
                for i in self.buttons[self.v]:
                    i='None'
                    
            
        def submit():
            self.v+=1
            self.h=0
            check()
        def clear():
            if(self.h>0):
                self.buttons[self.v][self.h-1].destroy()
                self.buttons[self.v][self.h-1]='None'
                self.h-=1
                self.guess.pop(self.h)
        def play():
            self.root.destroy()
            start=MASTERMINDS()
            
        
        colours = Label(self.b_frame, text="COLOURS :)",bg="#74BDCB", fg="black", pady=12)
        colours.grid(row=1,column=2)
        red = Button(self.b_frame,bg="red",padx=15, pady=4, command=lambda: button_click("red"))
        red.grid(row=5,column=2)
        blue = Button(self.b_frame,bg="blue",padx=15, pady=4, command=lambda: button_click("blue"))
        blue.grid(row=5,column=7)
        green = Button(self.b_frame,bg="green",padx=15, pady=4, command=lambda: button_click("green"))
        green.grid(row=8,column=2)
        yellow = Button(self.b_frame,bg="yellow",padx=15, pady=4, command=lambda: button_click("yellow"))
        yellow.grid(row=8,column=7)
        white = Button(self.b_frame,bg="white",padx=15, pady=4, command=lambda: button_click("white"))
        white.grid(row=11,column=2)
        violet = Button(self.b_frame,bg="violet",padx=15, pady=4, command=lambda: button_click("violet"))
        violet.grid(row=11,column=7)
        orange= Button(self.b_frame,bg="orange",padx=15, pady=4, command=lambda: button_click("orange"))
        orange.grid(row=18,column=2)
        sub = Button(self.b_frame, text="Submit", padx=4,pady=4,command=submit)  
        sub.grid(row=19,column=2)
        exit_b = Button(self.root, text="Exit Game",padx=4,pady=4,command=self.exit)
        exit_b.pack(side=BOTTOM)
        clearb= Button(self.root, text="Clear",padx=4,pady=4,command=clear)
        clearb.place(x=90,y=319)
        play_again=Button(self.b_frame,text='Play again',padx=7,pady=4,command=play).grid(row=20,columnspan=7)
    
start=MASTERMINDS()
