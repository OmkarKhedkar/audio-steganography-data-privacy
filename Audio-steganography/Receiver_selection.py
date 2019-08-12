from tkinter import *
from tkinter import IntVar
User_id = 2
y = 0
def select_user1():
	y = 1
	master.destroy()
def select_user2():
	y = 2
	master.destroy()
def select_user3():
	y = 3
	master.destroy()
def select_user4():
	y = 4	
	master.destroy()

def selectReceiver():
	global master
	master =  Tk()
	user = IntVar()
	user.set(1)
	
	b1 = Radiobutton(master, text="User1",variable=user, value="1", command = select_user1)
	b1.pack(anchor=CENTER)

	b2 = Radiobutton(master, text="User2",variable=user, value="2", command = select_user2)
	b2.pack(anchor=CENTER)

	b3 = Radiobutton(master, text="User3",variable=user, value="3", command = select_user3)
	b3.pack(anchor=CENTER)

	b4 = Radiobutton(master, text="User4",variable=user, value="4", command = select_user4)
	b4.pack(anchor=CENTER)

	master.mainloop()

	
selectReceiver()
