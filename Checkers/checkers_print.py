def convert(strings):
	words = "";
	string_list = list();
	for i in strings:
		for j in i:
			words+=j;
		string_list.append(words);
		words = "";
	return string_list;

def board():
	val = True;
	string = list("|-------------------------------|");
	strings = list();
	strings.append(string);
	for j in range(0,8):
		string = list();
		for i in range(0, 17):
			if (i+1)%2 == 0 and val:
				val = False;
				string.extend(list(" * "));
			elif (i+1)%2 == 0 and not val:
				val = True;
				string.extend(list("   "));
			else:
				string.extend(list("|"));
		val = not val;
		strings.append(string);
		if j > 6:
			strings.append(list("|-------------------------------|"));
			continue;	
		strings.append(list("|---|---|---|---|---|---|---|---|"));
	return strings;

def print_board(string_list):
	count = 0;
	for i, val in enumerate(string_list):
		if (i+1)%2 == 0:
			print(f"{count+1} {val}");
			count+=1;
		else:
			print(f"  {val}");
		if i > 15:
			print("    A   B   C   D   E   F   G   H  ");
def update(arraycheckers_real, strings, boolean):
	
	for i in arraycheckers_real:

		if strings[i[0]][i[1]] == "*":
			if boolean:
				strings[i[0]][i[1]] = "O";
			elif not boolean:
				
				strings[i[0]][i[1]] = "0";
	return strings;
def move(pos, later, listR, listB):
	print(listR);
	print(listB);
	for i, val in enumerate(listR):
		if val == pos:
			listR.pop(i);
			listR.insert(i, later);
			return True;
	for j, item in enumerate(listB):
		if item == pos:
			listB.pop(j);
			listB.insert(j, later);
			return True;
	return False;
strings = board();
string_list = convert(strings);


arraypos = list();
for j in range(1, len(string_list), 2):
	skip = 0;
	thing = True;
	for k in range(round(len(string_list[1])/4)):
		if thing:
			skip = k+2;
			arraypos.append([j, skip]);
			thing = False;
			continue;
		skip += 4;
		arraypos.append([j,skip]);
	
arraypoten = list();
arraypoten_real = list();
for i in arraypos:
	if strings[i[0]][i[1]] == "*":
		arraypoten.append([round((i[0] + 1)/2),round((i[1]+2)/4)]);
		arraypoten_real.append([i[0],i[1]]);
arraycheckersR = list();
arraycheckersB = list();
arraycheckersR_real = list();
arraycheckersB_real = list();
for i in arraypoten_real:

	if strings[i[0]][i[1]] == "*" and i[0] < 6:
		strings[i[0]][i[1]] = "O";
		arraycheckersR_real.append([i[0],i[1]]);
		arraycheckersR.append([round((i[0] + 1)/2),round((i[1]+2)/4)]);
	elif  strings[i[0]][i[1]] == "*" and i[0] > 10:
		strings[i[0]][i[1]] = "0";
		arraycheckersB_real.append([i[0],i[1]]);
		arraycheckersB.append([round((i[0] + 1)/2),round((i[1]+2)/4)]);
loop = True;
	
strings = board();
strings = update(arraycheckersR_real, strings, True);
strings = update(arraycheckersB_real, strings, False);
string_list = convert(strings);
while loop:
	print_board(string_list);
	print("Move a piece");
	userin = input();
	userin = userin.split(" ");
	pos = list(userin[0]);
	later = list(userin[1]);
	
	pos[0] = 2*int(pos[0]) - 1;
	later[0] = 2*int(later[0]) - 1;
	pos[1] = 4*int(pos[1]) - 2;
	later[1] = 4*int(later[1]) - 2;
	print(pos);
	print(later);
	if move(pos, later, arraycheckersR_real, arraycheckersB_real):
		strings = board();
		strings = update(arraycheckersR_real, strings, True);
		strings = update(arraycheckersB_real, strings, False);
		string_list = convert(strings);
		print_board(string_list);
		continue;
	else:
		print("Invalid move");
		continue;
