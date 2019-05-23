import random
loop = True
array = ["Rock", "Paper", "Scizors"]
while loop:
	rand = random.randint(0, 2)
	print("Choose Rock Paper or Scizors")
	userin = input()
	print("\n\n")

	if userin != "Rock" and userin != "Paper" and userin != "Scizors":
		if userin == "bye":
			print("Bye!\n\n")
			loop = False
		else:
			print("Invalid input champ\n\n")
			continue
	
	elif array[rand] == userin:
		print(f"The computer chose: {array[rand]}")
		print("Draw\n\n")
		continue
	elif (rand == 0 and userin != "Paper") or (rand == 1 and userin != "Scizors") or(rand == 2 and userin != "Rock"):
		print(f"The computer chose: {array[rand]}")
		print("Computer Wins!\n\n")
		continue
	elif (rand == 0 and userin == "Paper") or (rand == 1 and userin == "Scizors") or(rand == 2 and userin == "Rock"):
		print(f"The computer chose: {array[rand]}")
		print("You Win!\n\n")
		continue
