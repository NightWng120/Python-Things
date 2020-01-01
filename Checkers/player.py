import string;

class Player:
	my_pos = list();

	def __init__(self, color, first):
		self.color = color;
		self.first = first;

	def convert(self,strings):
		words = "";
		string_list = list();
		for i in strings:
			for j in i:
				words+=j;
			string_list.append(words);
			words = "";
		return string_list;

	def board(self):
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

	def print_board(self,string_list):
		count = 0;
		for i, val in enumerate(string_list):
			if (i+1)%2 == 0:
				print(f"{count+1} {val}");
				count+=1;
			else:
				print(f"  {val}");
			if i > 15:
				print("    A   B   C   D   E   F   G   H  ");
	def update(self,arraycheckers_real, strings, boolean):
		
		for i in arraycheckers_real:

			if strings[i[0]][i[1]] == "*":
				if boolean:
					strings[i[0]][i[1]] = "O";
				elif not boolean:
					
					strings[i[0]][i[1]] = "0";
		return strings;
	def move(self,pos, later, listR, listB):
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
	def user_in(self,userin):
		alpha = string.ascii_lowercase
		pos = list(userin[0]);
		later = list(userin[1]);
		out = [False,False];
		for i in alpha:
			print(f"Pos[0]: {pos[0].isalpha()}\nPos[1]: {pos[1].isalpha()}\n");
			print(f"Later[0]: {later[0].isalpha()}\nLater[1]: {later[1].isalpha()}\n");
			if i == pos[1] and pos[1].isalpha() and not pos[0].isalpha():
				print("Inside pos if");
				pos[1] = 4*((ord(i) - ord('h')) + 8)-2;
				pos[0] = 2*int(pos[0]) - 1;
				out[0] = True;
			if i == later[1] and later[1].isalpha() and not later[0].isalpha():
				print("Inside later if");
				later[1] = 4*((ord(i) - ord('h')) + 8)-2;
				later[0] = 2*int(later[0]) - 1;
				out[1] = True;
		if(out[0] and out[1]):	
			return pos, later;
		else:
			return False,False;
	def gen(self,string_list, strings,color):
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


		if(color == "Red"):
			return arraycheckersR_real,arraycheckersB_real;

		elif(color == "Black"):

			return arraycheckersB_real,arraycheckersR_real;



	def play(self, player):
		strings = list();
		strings = self.board();
		string_list = self.convert(strings);
		if self.first:
			self.my_pos, temp = self.gen(string_list, strings,self.color);
			self.first = False;
		elif not self.first:
			self.my_pos, temp = self.gen(string_list, strings,self.color);
			temp = list();
			temp = player.my_pos;
		loop = True;
			
		strings = self.board();
		strings = self.update(self.my_pos, strings, True);
		strings = self.update(temp, strings, False);
		string_list = self.convert(strings);
		while loop:
			self.print_board(string_list);
			print("Move a piece");
			userin = input();
			if userin == "quit":
				return 0;
			userin = userin.split(" ");
			print("Userin[0]: " + userin[0]);
			print("Userin[1]: " + userin[1]);
			pos, later = self.user_in(userin);
			print(pos);
			print(later);
			if not pos:
				print("Invalid input")
				continue;
			if self.move(pos, later, self.my_pos, temp):
				strings = self.board();
				strings = self.update(self.my_pos, strings, True);
				strings = self.update(temp, strings, False);
				string_list = self.convert(strings);
				self.rint_board(string_list);
				return True;
			else:
				print("Invalid move");
				continue;
