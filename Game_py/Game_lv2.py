print ("==============WELCOME TO LEVEL 2==========")
print ("====================GUESS NO. BETWEEN 0-30 ==================")

import random 
x = random.randint(0 , 30)
i = 0
a = int(input("Enter a value = "))
while a != x:
	if a < x :
		print("Enter a LARGER number ")
	if a > x:
		print("Enter a SMALLER number")
	i += 1	
	a = int(input("Enter a value = "))
if a == x:
	print("=================================CONGRATULATIONS YOU  HAVE WON LEVEL 2 ==========================")
	print("ATTEMPTS =", i)

	choice = input("CONTINUE TO NEXT LEVEL  : Y/N :- ")
	if choice == 'y':
		import Game_lv3.py
	else :
		print("....THANKYOU FOR PLAYING...")

