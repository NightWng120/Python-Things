def convert(strings):
	words = "";
	string_list = list();
	for i in strings:
		for j in i:
			words+=j;
		string_list.append(words);
		words = "";
	return string_list;
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
string_list = convert(strings);
arraypos = list();
count = 0;
for i, val in enumerate(string_list):
	if (i+1)%2 == 0:
		print(f"{count+1} {val}");
		count+=1;
	else:
		print(f"  {val}");
	if i > 15:
		print("    A   B   C   D   E   F   G   H  ");
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
print(arraypos);
print(len(arraypos));
	
arraypoten = list();
arraypoten_real = list();
for i in arraypos:
	if strings[i[0]][i[1]] == "*":
		arraypoten.append([round((i[0] + 1)/2),round((i[1]+2)/4)]);
		arraypoten_real.append([i[0],i[1]]);
print(arraypoten);
print();
print(arraypoten_real);
arraycheckers = list();
for i in arraypoten_real:

	if strings[i[0]][i[1]] == "*" and i[0] < 6:
		strings[i[0]][i[1]] = "O";
		arraycheckers.append([i[0],i[1]]);
	elif  strings[i[0]][i[1]] == "*" and i[0] > 10:
		strings[i[0]][i[1]] = "0";
		arraycheckers.append([i[0],i[1]]);
for i in strings:
	print(i);
print(arraycheckers);
string_list = convert(strings);
for i in string_list:
	print(i);
		
