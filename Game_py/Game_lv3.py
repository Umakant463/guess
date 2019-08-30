print ("=============  WELCOME TO PHASE OF GAME  ==========")

import random
o = random.randint(1, 50)
x = random.randint(0 , 50)
i = 0
a = int(input("Enter a value = "))
while a != x:
	x = random.randint(0 , 50)
	if a < x :
		print("Enter a LARGER number ")
	if a > x:
		print("Enter a SMALLER number")
	i += 1	
	a = int(input("Enter a value = "))
if a == x:
	print("=================================CONGRATULATIONS YOU  HAVE WON LEVEL 3 ==========================")
	print("ATTEMPTS = ", i)
else :
	print("THANK YOU FOR PLAYING !!!")