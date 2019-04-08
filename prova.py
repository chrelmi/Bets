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
window=Tk()
window.title("Picchetto tecnico")
window.geometry("800x400")
window.mainloop()


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

squadracs=input("\nInserisci la squadra di casa:  ")
squadratr=input("Inserisci la squadra in trasferta:  ")
file=input("File:  ")
file=file+".csv"
#picchetto tecnico
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
#calcolo quote reali
print("----------------------------------------------------------------------------------------------")
uno=input("Quota 1: ")
uno=float(uno)
x=input("Quota x: ")
x=float(x)
due=input("Quota 2: ")
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

