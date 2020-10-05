import random

#Function To display the tic tac toe list/board
def display_list(initial_list):
	print(initial_list[1]+'|'+initial_list[2]+'|'+initial_list[3])
	print(initial_list[4]+'|'+initial_list[5]+'|'+initial_list[6])
	print(initial_list[7]+'|'+initial_list[8]+'|'+initial_list[9])

#Function To take user input
def player_input():
	choice='string'
	while choice not in ['X','O']:

		choice=input('Player1:Choose X or O?')

		if choice=='X':
			return ('X','O')
		else:
			return ('O','X')
		
			if choice not in ['X','O']:
				print("Sorry ! Invalid Choice. Select 'X' or 'O'")

	return choice

#Function To add the user input to list
def replace_value(initial_list,choice,position):
	initial_list[position]=choice
	return initial_list

#Function To check whether user has won the game
def win_check(initial_list,choice):
	return ((initial_list[1]==initial_list[2]==initial_list[3]==choice) or
	(initial_list[4]==initial_list[5]==initial_list[6]==choice) or
	(initial_list[7]==initial_list[8]==initial_list[9]==choice) or
	(initial_list[1]==initial_list[4]==initial_list[7]==choice) or
	(initial_list[2]==initial_list[5]==initial_list[8]==choice) or
	(initial_list[3]==initial_list[6]==initial_list[9]==choice) or
	(initial_list[1]==initial_list[5]==initial_list[9]==choice) or
	(initial_list[7]==initial_list[5]==initial_list[3]==choice))

#Function to randomly select the player turn
def choose_first():
	flip=random.randint(0,1)
	if flip==0:
		return "Player 1"
	else:
		return "Player 2"

#Function to check the available position in list at the user specified position
def space_check(initial_list,position):
	return initial_list[position]==' '

#Function To check whether list is empty
def full_list_check(initial_list):
	for i in range(1,10):
		if space_check(initial_list,i):
			return False
	return True

#Function to take user input for filling the desired position
def player_choice(initial_list):
	position=0

	while position not in range(1,10) or not space_check(initial_list, position):
		position=int(input('Choose a position(1-9):'))

		if position not in range(1,10):
			print("Sorry ! Invalid Choice. Select number in range(1-9)")
	return position

#Function to ask player for game continuation
def replay():
	ready='Nothing'
	while ready not in ['Yes','No']:
		ready=input('Play again? Enter Yes or No:')
			

		if ready not in ['Yes','No']:
			print("Sorry ! Invalid Choice. Select 'Yes' or 'No'")
	return ready

#Logic for game play for player 1 and player 2
print("Welcome to Tic Tac Toe!")
while True:
	initial_list=[' ']*10
	player1_choice,player2_choice=player_input()
	turn = choose_first()
	print(turn + ' will go first!')

	play_game=input('Ready to play?y or n')

	if play_game=='y':
		game_on=True
	else:
		game_on=False

	while game_on:
		if turn =='Player 1':
			display_list(initial_list)
			position=player_choice(initial_list)
			replace_value(initial_list, player1_choice, position)

			if win_check(initial_list, player1_choice):
				display_list(initial_list)
				print('Player 1 has WON!!!!')
				game_on=False

			else:
				if full_list_check(initial_list):
					display_list(initial_list)
					print("Tie Game")
					game_on=False

				else:
					turn="Player 2"

		else:
			display_list(initial_list)
			position=player_choice(initial_list)
			replace_value(initial_list, player2_choice, position)

			if win_check(initial_list, player2_choice):
				display_list(initial_list)
				print('Player 2 has WON!!!!')
				game_on=False

			else:
				if full_list_check(initial_list):
					display_list(initial_list)
					print("Tie Game")
					game_on=False

				else:
					turn="Player 1"
	if not replay():
		break




