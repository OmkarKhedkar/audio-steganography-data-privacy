#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    Apr 21, 2019 05:59:20 PM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


import algo_popup_support

def Vp1_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    algo_popup_support.init(root, top)
    root.mainloop()

w = None
z = 0
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    algo_popup_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    v = 1
    def close_window(self):
        file = open('select_audio.txt','w')
        file.write(str(self.v))
        file.close()
        global z
        z = self.v
        root.destroy();

    def select_lsb(self):
        self.v = 1
        self.Radiobutton2.deselect()
    def select_ss(self):
        self.v = 2
        self.Radiobutton1.deselect()
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+650+150")
        top.title("Choose Embedding Technique")
        top.configure(background="#d9d9d9")

        self.Radiobutton1 = tk.Radiobutton(top)
        self.Radiobutton1.place(relx=0.1, rely=0.2, relheight=0.056
                , relwidth=0.083)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(text='''WAV''')
        self.Radiobutton1.configure(variable = self.v)
        self.Radiobutton1.configure(value = '1')
        self.Radiobutton1.configure(command = self.select_lsb)
        self.Radiobutton1.select()

        self.Radiobutton2 = tk.Radiobutton(top)
        self.Radiobutton2.place(relx=0.483, rely=0.2, relheight=0.056
                , relwidth=0.197)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''MP3''')
        self.Radiobutton2.configure(variable = self.v)
        self.Radiobutton2.configure(value = '2')
        self.Radiobutton2.configure(command = self.select_ss)
        
        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.317, rely=0.356, height=44, width=77)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''OK''')
        self.Button1.configure(width=77)
        self.Button1.configure(command = self.close_window)

def cc():
    Vp1_start_gui()
    return z 
