import random
print ("====================WELCOME TO MY GUESSING GAME==================")
print ("====================GUESS NO. BETWEEN 0-10 ==================")

x = random.randint(0 , 10)
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
	print("=================================CONGRATULATIONS YOU HAVE WON==========================")
	print("ATTEMPTS =", i)

	choice = input("CONTINUE TO NEXT LEVEL  : Y/N :- ")
	if choice == 'y':
		import Game_lv2.py
	else :
		print("THANK YOU FOR PLAYING !!!")


	

