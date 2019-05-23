
current = 1
previous = 1
for i in range(1, 20):
	
	if i == 1:
		print(i)
		continue

	
	print(f"{current}")
	temp = current
	current += previous

	previous = temp
