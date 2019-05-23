import random

loop = True
loop2 = True
x = 0
while loop:
	rand = random.randint(1, 10)
	while loop2:
		x+=1
		userin = input("Guess a number between 1 and 10: ")
		if int(userin) < rand:
			print("Too low!")
			continue
		elif int(userin) > rand:
			print("Too high!")
			continue
		elif int(userin) == rand:
			print(f"You won! in {x} tries!")
			input()
			break 
		else:
			print("Invalid Input")
	userin = input("Would you like to play again? (y/n): ")
	x = 0
	if userin == "y" or userin == "Y":
		loop2 = True
		continue
	elif userin == "n" or userin == "N":
		loop = False
	else:
		print("Invalid input")
		loop2 = False
		continue
		
