loop = True;
factor = 1.609
while loop:

	try
		print("Would you like to convert Kilometers or Miles?")
		userin = input()	
		if userin == "Kilometers" or userin == "kilometers":
			# Dank memes
			print("Please enter how many Kilometers you ran")
			j = input()
			result = round((1/factor) * float(j), 2)
			print(f"You ran {result} miles")
			continue
		elif userin == "Miles" or userin == "miles":
			print("Please enter how many Miles you ran")
			x = input()
			product = round((factor) * float(x), 2)
			print(f"You ran {product} kilometers")
			continue
		elif userin == "Gay":
			loop = False

	except Some:
