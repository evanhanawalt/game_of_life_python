import GameBoard

def print_board(board):
	for i in range(0,board.rows):
		for j in range(0,board.columns):
			if( board.get(i,j) ):
				print("*", end = '')
			else:
				print("_", end = '')
		print("")

board = GameBoard.GameBoard()

print("blank initialization")
print_board(board)


board.set(1,1,True)
board.set(2,1,True)
board.set(3,1,True)
print("set values")
print_board(board)


board.update()
print("after update")
print_board(board)


board.update()
print("after update")
print_board(board)
