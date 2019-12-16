val = True;
string = "|-------------------------------|";
strings = list();
strings.append(string);
for j in range(0,8):
	string = "";
	for i in range(0, 17):
		if (i+1)%2 == 0 and val:
			val = False;
			string+= " * ";
		elif (i+1)%2 == 0 and not val:
			val = True;
			string+= "   ";
		else:
			string+= "|";
	val = not val;
	strings.append(string);
	if j > 6:
		strings.append("|-------------------------------|");
		continue;	
	strings.append("|---|---|---|---|---|---|---|---|");
arraypos = list();
count = 0;
for i, val in enumerate(strings):
	if (i+1)%2 == 0:
		print(f"{count+1} {val}");
		count+=1;
	else:
		print(f"  {val}");
	if i > 15:
		print("    A   B   C   D   E   F   G   H  ");
for j in range(1, len(strings), 2):
	skip = 0;
	thing = True;
	for k in range(round(len(strings[1])/4)):
		if thing:
			skip = k+2;
			arraypos.append([j, skip]);
			thing = False;
			continue;
		skip += 4;
		arraypos.append([j,skip]);
print(arraypos);
print(len(arraypos));
arraycheckers = list();
arraycheckers_real = list();
for i in arraypos:
	if strings[i[0]][i[1]] == "*":
		arraycheckers.append([round((i[0] + 1)/2),round((i[1]+2)/4)]);
		arraycheckers_real.append([i[0],i[1]]);
print(arraycheckers);
print();
print(arraycheckers_real);

for i in arraycheckers_real:

	if strings[i[0]][i[1]] == "*" and i[0] < 6:
		strings[i[0]] = strings[i[0]].replace("*", "O");

	elif  strings[i[0]][i[1]] == "*" and i[0] > 10:
		strings[i[0]] = strings[i[0]].replace("*", "0");
for i in strings:
	print(i);



		
