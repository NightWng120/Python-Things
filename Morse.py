import string
alphaL = string.ascii_lowercase
alphaU = string.ascii_uppercase
code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."];
loop = True


def morse(string):
	out = "";
	for val in string:
		for j, item in enumerate(alphaL):
			if val.lower() == item:
				out += " " + code[j];
		if val == " ":
			out += "/ ";
				

	out += "//"
	return out;
def alpha(string):
	
	words = string.split('/');
	string = "";
	for val in words:
		letters = val.split(' ');
		for item in letters:
			for i, element in enumerate(code):

				if item == element:
					string += alphaU[i];
		string += " ";
		
	return string;

	

while loop:

	print("|-------------------------|");
	print("|  Morse Code Translator  |");
	print("|-------------------------|");
	print("| 1) Alphabetical to morse|");
	print("| 2) Morse to alphabetical|");
	print("| 3) Exit                 |");
	print("|-------------------------|");
	print("\n");
	print(f": ", end='');
	userin = input()
	if userin == "1":
		print("\nEnter your string to be converted to Morse Code");
		userin = input();		
		userin = morse(userin);
		print(f"Your Morse Code string is: \n{userin}\n\n");
		continue;
	elif userin == "2":
		print("\nEnter your string to be converted to Morse Code");
		userin = input();		
		userin = alpha(userin);
		print(f"Your Morse Code string is: \n{userin}\n\n");
		continue;

	elif userin == "3":
		print("\n\nClosing Morse Code Translator.......\n\n");
		loop = False;
		continue;

	else:
		print("***Invalid Input***");
		continue;


		
