import numpy as np

# compter is 2, person is 1

def num_to_char(num):
	if num == 0:
		return ' '
	if num == 1:
		return 'O'
	if num == 2:
		return 'X'
def print_board(pboard):
	print(f"{num_to_char(pboard[0,0])} | {num_to_char(pboard[0,1])} | {num_to_char(pboard[0,2])}")
	print(f"{num_to_char(pboard[1,0])} | {num_to_char(pboard[1,1])} | {num_to_char(pboard[1,2])}")
	print(f"{num_to_char(pboard[2,0])} | {num_to_char(pboard[2,1])} | {num_to_char(pboard[2,2])}")


def get_spots(board):
	valList = []
	vals = np.where(board == 0)
	for i in range(len(vals[0])):
		valList.append((vals[0][i], vals[1][i]))
	return valList

def check_if_winn(board):
	slantAxis = np.array([[board[0,0], board[1,1], board[2,2]], [board[0,2], board[1,1], board[2,0]]]).reshape(2,3)

	oRowWin = np.all((board == 1), axis=1)
	oColWin = np.all((board == 1), axis=0)
	xRowWin = np.all((board == 2), axis=1)
	xColWin = np.all((board == 2), axis=0)

	oSlantWin = np.all((slantAxis == 1), axis=1)
	xSlantWin = np.all((slantAxis == 2), axis=1)

	if np.any(oRowWin == True):
		return 1
	if np.any(oColWin == True):
		return 1
	if np.any(xRowWin == True):
		return 2
	if np.any(xColWin == True):
		return 2

	if np.any(oSlantWin == True):
		return 1
	if np.any(xSlantWin == True):
		return 2

	return 0



def move(board):
	x = None
	y = None

	options = get_spots(board)

	for boardOptions in options:
		x,y = boardOptions
		boardCopy = np.array(board, copy=True)

		# defensive
		boardCopy[x,y] = 1
		if check_if_winn(boardCopy) == 1:
			boardCopy[x,y] = 2
			return x,y

		# offensive
		boardCopy[x,y] = 2
		if check_if_winn(boardCopy) == 2:
			boardCopy[x,y] = 2
			return x,y
	
	# unintelligent next move
	x,y = options[0]

	# more intelligent next move

	return x, y


# print(print_board(board))
# print(get_spots(board))

# x,y = move(board)
# board[x,y] = 2
# print_board(board)



# def find_move(board):
# 	options = get_spots(board)
# 	maxOpportinty = []
# 	for i in range(len(options)):
# 		x,y = options[i]
# 		boardCopy = np.array(board, copy=True)
# 		boardCopy[x,y] = 2
# 		maxOpportinty.append(get_opportunity(boardCopy))

# 	max(maxOpportinty) = index
# 	x,y = options[index]


# def get_opportunity(board):
# 	slantAxis = np.array([[board[0,0], board[1,1], board[2,2]], [board[0,2], board[1,1], board[2,0]]]).reshape(2,3)

# 	oRowUsed = np.all((board == 1), axis=1)
# 	oColUsed = np.all((board == 1), axis=0)
# 	oSlantUsed = np.all((slantAxis == 1), axis=1)

# 	np.any(xRowWin == False)
# 	np.any(xRowWin == False)
# 	np.any(xRowWin == False)
	






