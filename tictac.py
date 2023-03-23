import numpy as np
import os
import computer

# 0 => empty
# 1 => O
# 2 => X

board = np.zeros((3,3))

def check_if_win():
	slantAxis = np.array([[board[0,0], board[1,1], board[2,2]], [board[0,2], board[1,1], board[2,0]]]).reshape(2,3)

	oRowWin = np.all((board == 1), axis=1)
	oColWin = np.all((board == 1), axis=0)
	xRowWin = np.all((board == 2), axis=1)
	xColWin = np.all((board == 2), axis=0)

	oSlantWin = np.all((slantAxis == 1), axis=1)
	xSlantWin = np.all((slantAxis == 2), axis=1)

	if np.any(oRowWin == True):
		return 'O (You) Wins!'
	if np.any(oColWin == True):
		return 'O (You) Wins!'
	if np.any(xRowWin == True):
		return 'X (Computer) Wins!'
	if np.any(xColWin == True):
		return 'X (Computer) Wins!'
	if np.any(oSlantWin == True):
		return 'O (You) Wins!'
	if np.any(xSlantWin == True):
		return 'X (Computer) Wins!'

	if len(computer.get_spots(board)) == 1:
		return 'Draw!'

def num_to_char(num):
	if num == 0:
		return ' '
	if num == 1:
		return 'O'
	if num == 2:
		return 'X'

def print_board():
	print(f"{num_to_char(board[0,0])} | {num_to_char(board[0,1])} | {num_to_char(board[0,2])}")
	print(f"{num_to_char(board[1,0])} | {num_to_char(board[1,1])} | {num_to_char(board[1,2])}")
	print(f"{num_to_char(board[2,0])} | {num_to_char(board[2,1])} | {num_to_char(board[2,2])}")

def convert_input(player):
	validInput = False
	input1 = None
	input2 = None
	x = 0
	y = 0

	while not validInput:
		try:
			input1, input2  = input(f'Player {str(player)}: ')
			validInputs = ['l', 'm', 'r', 't', 'b']
			if str(input1).lower() in validInputs:
				input1 = input1.upper()
				validInput = True
			if str(input2).lower() in validInputs:
				input2 = input2.upper()
				validInput = True
		except ValueError:
			validInput = False

	#y:   0   1   2   x:
	  # TL | TM | TR  0
	  # ML | MM | MR  1
	  # BL | BM | BR  2

	if(input1 == 'M' and input2 == 'M'):
		return 1, 1
	
	if((input1 == 'M' or input2 == 'M') and (input1 == 'T' or input2 == 'T')):
		return 0, 1

	if((input1 == 'M' or input2 == 'M') and (input1 == 'B' or input2 == 'B')):
		return 2, 1
	
	if((input1 == 'M' or input2 == 'M') and (input1 == 'L' or input2 == 'L')):
		return 1, 0

	if((input1 == 'M' or input2 == 'M') and (input1 == 'R' or input2 == 'R')):
		return 1, 2

	if(input1 == 'L' or input2 == 'L'):
		y = 0
	if(input1 == 'R' or input2 == 'R'):
		y = 2
	if(input1 == 'T' or input2 == 'T'):
		x = 0
	if(input1 == 'B' or input2 == 'B'):
		x = 2

	return x, y

def get_input(player):
	x, y = convert_input(player)
	while (not board[x,y] == 0):
		x, y = convert_input(player)
	return x, y

print("TL | TM | TR \nML | MM | MR \nBL | BM | BR")
print('')

while True:
	print_board()
	if check_if_win():
		print(check_if_win())
		break
	x,y = get_input('O (You)')
	board[int(x),int(y)] = 1
	os.system('cls||clear')
	
	# check_if_win()
	# print_board()
	# x,y = get_input('X (Computer)')
	x, y = computer.move(board)
	board[int(x),int(y)] = 2
	print('Computer move:')

	# os.system('cls||clear')




# board[0] = [1,2,2]
# board[1] = [1,2,1]
# board[2] = [2,1,1]

