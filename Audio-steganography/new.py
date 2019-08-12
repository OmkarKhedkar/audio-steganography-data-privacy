from tkinter import *
from tkinter import IntVar
User_id = 2
w = 0

def select_user1():
	w = 1
	master.destroy()
def select_user2():
	w = 2
	master.destroy()
def select_user3():
	w = 3
	master.destroy()
def select_user4():
	w = 4	
	master.destroy()

def selectReceiver():
	master = Tk()
	MODES = [
		("User1", "1"),
		("User2", "2"),
		("User3", "3"),
		("User4", "4"),
		]

	v = IntVar()
	v.set(0)
	
	b1 = Radiobutton(master, text="User1",variable=v, value="1", command = select_user1)
	b1.pack(anchor=CENTER)

	b2 = Radiobutton(master, text="User2",variable=v, value="2", command = select_user2)
	b2.pack(anchor=CENTER)

	b3 = Radiobutton(master, text="User3",variable=v, value="3", command = select_user3)
	b3.pack(anchor=CENTER)

	b4 = Radiobutton(master, text="User4",variable=v, value="4", command = select_user4)
	b4.pack(anchor=CENTER)

	master.mainloop()		