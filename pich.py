#!/usr/bin/env python3
import tkinter
from tkinter import *
import csv
import time
from datetime import datetime
from decimal import Decimal

countcs=0
countvc=0
countr=0
countptr=0
countpcs=0
countvtr=0
vcs=0
vtr=0
pc=0
cs=0
vc=0
tr=0
ptr=0
vt=0
camp=" "
file=" "
squadracs=" "
squadratr=" "

def seriea():
	camp="italiaA.csv"
	update(camp)
def serieb():
	camp="italiaB.csv"
	update(camp)
def premier():
	camp="inghilterra.csv"
	update(camp)
def ligue1():
	camp="francia.csv"
	update(camp)
def bundes():
	camp="germania.csv"
	update(camp)
def laliga():
	camp="spagna.csv"
	update(camp)
def jupiler():
	camp="belgio.csv"
	update(camp)
def hnl():
	camp="croazia.csv"
	update(camp)
def superleague():
	camp="grecia.csv"
	update(camp)
def superlig():
	camp="turchia.csv"
	update(camp)
def premierR():
	camp="russia.csv"
	update(camp)
def primiera():
	camp="portogallo.csv"
	update(camp)
def eredivise():
	camp="olanda.csv"
	update(camp)
def update(file):
	print(file)
	l=tkinter.Label(root,text="Quota 1",bg="#000000",fg="#FFFFFF")
	l.config(font=("Noto Sans Mono CJK JP Bold", 24))
	l.grid(row=0,column=3, padx=10)
	l2=tkinter.Label(root,text="Quota X",bg="#000000",fg="#FFFFFF")
	l2.config(font=("Noto Sans Mono CJK JP Bold", 24))
	l2.grid(row=1,column=3, padx=10)
	l3=tkinter.Label(root,text="Quota 2",bg="#000000",fg="#FFFFFF")
	l3.config(font=("Noto Sans Mono CJK JP Bold", 24))
	l3.grid(row=2,column=3, padx=10)
	l4=tkinter.Label(root,text="Squadra Casa",bg="#000000",fg="#FFFFFF")
	l4.config(font=("Noto Sans Mono CJK JP Bold", 24))
	l4.grid(row=0,column=0, padx=10)
	l5=tkinter.Label(root,text="Squadra Ospite",bg="#000000",fg="#FFFFFF")
	l5.config(font=("Noto Sans Mono CJK JP Bold", 24))
	l5.grid(row=1,column=0, padx=10)	
	e1.grid(row=0,column=4)	
	e2.grid(row=1,column=4)
	e3.grid(row=2,column=4)	
	e4.grid(row=0,column=1) #Squadra Casa
	e5.grid(row=1,column=1) #squadra Trasferta
	b=Button(root, text="Invia", width=10, command=lambda:callback(file,squadracs,squadratr))
	b.grid(row=2,column=0,columnspan=2)
def callback(file,squadracs,squadratr):
	squadracs=tkinter.StringVar()
	squadracs=e4.get()
	print(squadracs)
	squadratr=tkinter.StringVar()
	squadratr=e5.get()
	print(squadratr)
	countcs=0
	countvc=0
	countr=0
	countptr=0
	countpcs=0
	countvtr=0
	vcs=0
	vtr=0
	pc=0
	cs=0
	vc=0
	tr=0
	ptr=0
	vt=0
	#picchetto tecnico
	print(squadracs+"-"+squadratr)
	print("FILE DA APRIRE"+file)
	with open(file) as csvfile:
		r=csv.DictReader(csvfile)
		for row in r:
			data=row['DATA']
			date=datetime.strptime(data,"%d/%m/%Y")
			casa=row['CASA']
			trasferta=row['TRASFERTA']
			if squadracs in casa or squadracs in trasferta:
				golcs=row['GOLCS']
				goltr=row['GOLTR']
				print(data+"  "+casa+"-"+trasferta+" "+golcs+"-"+goltr)
				if squadracs in casa:
					countcs=countcs+1
					if golcs>goltr:
						countvc=countvc+1
					if golcs<goltr:
						countpcs=countpcs+1

	print("----------------------------------------------------------------------------------------------")
	with open(file) as csvfile:
		r=csv.DictReader(csvfile)
		for row in r:
			data=row['DATA']
			date=datetime.strptime(data,"%d/%m/%Y")
			casa=row['CASA']
			trasferta=row['TRASFERTA']
			if squadratr in casa or squadratr in trasferta:
				golcs=row['GOLCS']
				goltr=row['GOLTR']
				print(data+"  "+casa+"-"+trasferta+" "+golcs+"-"+goltr)
				if squadratr in trasferta:
					countr=countr+1
					if goltr<golcs:
						countptr=countptr+1
					if goltr>golcs:
						countvtr=countvtr+1	
	print("----------------------------------------------------------------------------------------------")
	#calcolo quote reali	
	uno=e1.get() #input("Quota 1: ") #e1
	uno=float(uno)
	x=e2.get() #input("Quota x: ") #e2
	x=float(x)
	due=e3.get() #input("Quota 2: ") #e3
	due=float(due)
	uno=100/uno
	x=100/x
	due=100/due
	somma=(uno+x+due)/100
	uno=uno/somma
	x=x/somma
	due=due/somma
	uno=100/uno
	x=100/x
	due=100/due
	uno=round(uno,2)
	x=round(x,2)
	due=round(due,2)
	uno=str(uno)
	x=str(x)
	due=str(due)
	print("Quote reali:	1	X	2")
	print("               "+uno+"   "+x+"    "+due)
	print("----------------------------------------------------------------------------------------------")
	cs=countcs
	vc=countvc
	pc=countpcs
	countcs=str(countcs)
	countvc=str(countvc)
	countpcs=str(countpcs)
	print("Partite totali in casa "+squadracs+": "+countcs+"\nPartite vinte in casa "+squadracs+": "+countvc+"\nPartite perse in casa: "+countpcs)
	tr=countr
	ptr=countptr
	vt=countvtr
	countr=str(countr)
	countvtr=str(countvtr)
	countptr=str(countptr)
	print("\n\nPartite totali in trasferta "+squadratr+": "+countr+"\nVittorie perse in trasferta "+squadratr+": "+countptr+"\nPartite vinte in trasferta: "+countvtr)
	#calcolo picchetti
	picchettocs=(vc+ptr)/(cs+tr)
	picchettocs=picchettocs*100
	picchettotr=(pc+vt)/(cs+tr)
	picchettotr=picchettotr*100
	picchettocs=round(picchettocs,2)
	picchettotr=round(picchettotr,2)
	picchettox=100-(picchettocs+picchettotr)
	picchettox=round(picchettox,2)
	#calcolo quote
	quotacasa=100/picchettocs
	quotacasa=round(quotacasa,2)
	quotacasa=str(quotacasa)
	quotatr=100/picchettotr
	quotatr=round(quotatr,2)
	quotatr=str(quotatr)
	quotax=100/picchettox
	quotax=round(quotax,2)
	quotax=str(quotax)
	#stampe
	picchettox=str(picchettox)
	picchettocs=str(picchettocs)
	picchettotr=str(picchettotr)
	print("Pic 1: "+picchettocs+"%"+"\nPic X: "+picchettox+"%"+"\nPic 2: "+picchettotr+"%")
	print("QUOTE FINALI:     1       X       2")
	print("                "+quotacasa+"    "+quotax+"     "+quotatr)
#Definizione grafica
root=Tk()
root.geometry("800x400")
root.title("Calcolatore Picchetto Tecnico")
menu=Menu(root)
root.config(menu=menu)
subMenu=Menu(menu)
menu.add_cascade(label="Campionati", menu=subMenu)
subMenu.add_command(label="Serie A(ITA)",command=seriea)
subMenu.add_command(label="Serie B (ITA)",command=serieb)
subMenu.add_separator()
subMenu.add_command(label="Premier League (ING)",command=premier)
subMenu.add_command(label="Ligue 1 (FRA)",command=ligue1)
subMenu.add_command(label="Bundesliga (GER)",command=bundes)
subMenu.add_command(label="LaLiga (SPA)",command=laliga)
subMenu.add_command(label="Jupiler League (BEL)",command=jupiler)
subMenu.add_command(label="HNL (CRO)",command=hnl)
subMenu.add_command(label="Super League (GRE)",command=superleague)
subMenu.add_command(label="Super Lig (TUR)",command=superlig)
subMenu.add_command(label="Premier League (RUS)",command=premierR)
subMenu.add_command(label="Primiera Liga (POR)",command=primiera)
subMenu.add_command(label="Eredivise (HOL)",command=eredivise)
editMenu=Menu(menu)
root.configure(background="#000000")
e1=Entry(root)
#e1.grid(row=0,column=3)
e2=Entry(root)
#e2.grid(row=1,column=3)
e3=Entry(root)
#e3.grid(row=2,column=3)
e4=Entry(root)
#e4.grid(row=0,column=1) #Squadra Casa
e5=Entry(root)
#e5.grid(row=1,column=1) #squadra Ospite
root.mainloop()
