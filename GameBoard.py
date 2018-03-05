class GameBoard:

	def __init__(self, rows = 6, columns = 8, prevboard = None):
		self.board = []
		self.rows = rows
		self.columns = columns

		# initialize blank board
		for i in range(0, rows):
			self.board.append([])
			for j in range(0, columns):
				self.board[i].append(False)

		# fill from previous board if included in the constructor call
		if prevboard is not None:
			for i in range(0,rows):
				if i >= prevboard.rows:
					continue
				for j in range(0,columns):
					if j >= prevboard.columns:
						continue
					else:
						self.set(i,j,prevboard.get(i,j));


	def get(self, row, column):
		return self.board[row][column]

	def set(self, row, column, value):
		self.board[row][column] = value

	def number_live_neighbors(self, row, column):
		count = 0
		neighbor_rows = [row, row + 1, row - 1]
		neighbor_columns = [column, column + 1, column - 1]

		neighbor_indexes = [(x,y) for x in neighbor_rows
							for y in neighbor_columns
							# assert neighbor is in bounds
							if (0 <= x < self.rows)
							and (0 <= y < self.columns)
							 # assert neighbor is not the cell under test
							and not (x == row and y == column) ]

		# increment count for all live cells
		for cell in neighbor_indexes:
			if( self.get(cell[0],cell[1]) ):
				count += 1

		return count
				

	def update(self):
		new_board = []
		
		for i in range(0, self.rows):
			new_board.append([])
			for j in range(0, self.columns):
				live_neighbors = self.number_live_neighbors(i,j)

				if (live_neighbors < 2):
					new_board[i].append(False)
				elif (live_neighbors == 2):
					new_board[i].append(self.get(i,j))
				elif (live_neighbors == 3):
					new_board[i].append(True)
				elif (live_neighbors > 3):
					new_board[i].append(False)

		self.board = new_board












