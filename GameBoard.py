class GameBoard:
	def __init__(self, rows = 6, columns = 8, prevboard = None):
		self.board = []
		self.rows = rows
		self.columns columns

		for i in range(0, rows):
			self.board.append([])
			for j in range(0, columns):
				self.board[i].append(False)

		if prevboard is None:
			for i in range(0,rows):
				if i >= prevboard.rows:
					continue
				for j in range(0,columns):
					if j >= prevboard.columns:
						continue
					else:
						self.set(i,j,prevboard.get(i,j));


	def get(row, column):
		return self.board[row][column]

	def set(row, column, value):
		self.board[row][column] = value
