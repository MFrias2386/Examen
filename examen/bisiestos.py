#!/usr/bin/env python 
# - *- coding: utf- 8 - *-
def Bisiestos():
	x =int(input("inserta año:"))
	r = x % 4
	r100=x% 100
	r400=x%400
	if r ==0:
		print ("Es bisiesto")
	elif r100 ==0:
		print("Es Bisiesto")
	elif r400 ==0:
		print("Es Bisiesto")
	else:
	    print("No es Bisiesto")
    
    		
	
	
Bisiestos()
