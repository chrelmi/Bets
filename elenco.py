#!/usr/bin/env python3
import tkinter
from tkinter import *
import csv
import re

pan=Tk()
pan.geometry("400x400")
pan.title("Elenco ")
a=""
'''f=open("elenco.csv","r")
a=f.read()
b=" "
a=re.sub(',','  ',a)
print(a)'''
campionato="ItaliaA"
with open('elenco.csv') as csvfile:
	r=csv.DictReader(csvfile)
	a=a+campionato+"\n"
	for row in r:
		a=a+row[campionato]+"\n"
label=tkinter.Label(pan,text=a)
label.config(font=("Noto Sans Mono CJK JP Bold", 9))
label.config(justify=LEFT)
label.grid(row=0,column=0)
pan.mainloop()

