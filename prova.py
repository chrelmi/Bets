#!/usr/bin/env python3

#countcs=contatore partite casa
#countvc=contatore vittorie casa
#countr=contatore partite trasferta
#countvtr=contatore vittorie trasferte

import csv
import time
from datetime import datetime
from decimal import Decimal
import tkinter
from tkinter import *
import time

window=Tk()
window.title("Picchetto tecnico")
window.geometry("800x400")
def update():
	time.sleep(1)
	l.config(text="Roma")
window.configure(background="#000000")
l=tkinter.Label(window,text="Sampdoria",bg="#000000",fg="#FFFFFF")
l.config(font=("Noto Sans Mono CJK JP Bold", 24))
l.grid(row=0,column=0, padx=50)
t=tkinter.Label(window, bg="#000000", fg="#FFFFFF")
t.config(font=("Courier 10 Pitch",32))
t.grid(row=2,column=0)
b=Button(window, text="Invia", width=10, command=update)
b.grid(row=3)
window.mainloop()

