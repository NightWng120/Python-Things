import player

loop = True;
p1 = True;
p2 = True;
while loop:
	print("|-------------------------------|");
	print("|           Checkers            |");
	print("|-------------------------------|");
	print("|  Which player are you (1/2)?  |");
	print("|-------------------------------|");

	print("\n");
	print(": ", end = "");
	userin = input();
	if userin == "quit":
		loop = False;
		continue;
	if userin == "1":
		player1 = player.Player("Red", True);
		player2 = player.Player("Black", False);

		while p1 and p2:
			p1 = player1.play(player2);
			p2 = player2.play(player1);

	elif userin == "2":
		player1 = player.Player("Black", False);
		player2 = player.Player("Red", True);

		while p1 and p2:
			p2 = player2.play(player1);
			p1 = player1.play(player2);


