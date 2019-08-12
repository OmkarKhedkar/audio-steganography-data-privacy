from tkinter import *
import os
import Main as m
creds = 'Credentials.txt' # This just sets the variable creds to 'tempfile.temp'
lg = 0
def Login():
    global nameEL
    global pwordEL # More globals :D
    global rootA
 
    rootA = Tk() # This now makes a new window.
    rootA.title('Login') # This makes the window title 'login'
    rootA.geometry("250x150")
    intruction = Label(rootA, text='Please Login\n') # More labels to tell us what they do
    intruction.grid(sticky=E) # Blahdy Blah
 
    nameL = Label(rootA, text='Username: ') # More labels
    #nameL.pack(anchor = CENTER)
    pwordL = Label(rootA, text='Password: ') # ^
    #pwordL.pack(anchor = CENTER)
    nameL.grid(row=1)
    pwordL.grid(row=2)
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=100)
    pwordEL.grid(row=2, column=100)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(rowspan = 200, columnspan=450)
    rootA.mainloop()	
 
def CheckLogin():
    i = 0
    with open(creds) as f:
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        j = 1
        while(i < 7):
            uname = data[i].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
            pword = data[i + 1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
            if nameEL.get() == uname and pwordEL.get() == pword: # Checks to see if you entered the correct data.
                rootA.destroy()
                User_id = j
                print(j)
                lg = 1
                m.vp_start_gui()
            j = j + 1    
            i = i + 2
        if i == 8 and lg == 0:
            r = Tk()
            r.title('D:')
            r.geometry('150x50')
            rlbl = Label(r, text='\n[!] Invalid Login')
            rlbl.pack()
            r.mainloop()
 
Login()
