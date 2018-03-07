import tkinter as tk
from GameBoard import GameBoard
class GameOfLifeApp(tk.Frame):
	''' An example application for TkInter.  Instantiate
		and call the run method to run. '''
	def __init__(self, master, board):
		# Initialize window using the parent's constructor
		tk.Frame.__init__(self,
						  master,
						  width=630,
						  height=490)
		# set data model
		self.board = board
		self.is_running = False

		# Set the title
		self.master.title('Game of Life')
 
		# This allows the size specification to take effect
		self.pack_propagate(0)
 
		# We'll use the flexible pack layout manager
		self.pack()

		# Game board frame 
		self.top_frame = tk.Frame(self, width=630, height=450, background="#e9e9e9")
		self.top_frame.pack(fill=tk.BOTH, expand=True, anchor="c", padx=20, pady=20)

		# Create cells based on board dimensions
		self.cells = []
		for i in range(0, board.rows):
			self.cells.append([])
			for j in range(0, board.columns):
				self.cells[i].append(tk.Button(self.top_frame,
									width='1', height='1',
									text=' ',
									command= lambda row=i, column=j: self.update_cell(row,column))
				)
				self.cells[i][j].grid(row=i,column=j)



		# Buttons and Button Frame
		self.bottom_frame = tk.Frame(width=630, height=50,)
		self.bottom_frame.pack(side=tk.BOTTOM)

		# The start/stop button
		self.start_stop_button = tk.Button(self.bottom_frame,
								   text='Start',
								   command=self.start_stop_game)

		# The iterate button
		self.iterate_button = tk.Button(self.bottom_frame,
								   text='>',
								   command=self.iterate_game)

		# The clear button
		self.clear_button = tk.Button(self.bottom_frame,
								   text='Clear',
								   command=self.clear)

		# Put the controls on the frame
		self.start_stop_button.pack(side=tk.LEFT)
		self.iterate_button.pack(side=tk.LEFT)
		self.clear_button.pack(side=tk.LEFT)	
 
	def print_out(self):
		''' Print a greeting constructed
			from the selections made by
			the user. '''
		print('gvvdfasd, asdfasd!')


	def clear(self):
		# clear data model
		self.board = GameBoard(rows=16, columns=16)
		# update view
		self.update_board()

	def iterate_game(self):
		# update data model
		self.board.update()
		# update view
		self.update_board()

	def start_stop_game(self):
		print()
		# determine if game is running
		# if running, set event to stop, set running = false
		# if not running, set event to start, set running  = true

	def update_board(self):
		for row in range(0,self.board.rows):
			for column in range(0,self.board.columns):
				if self.board.get(row, column):
					self.cells[row][column]['text'] = 'X'
				else:
					self.cells[row][column]['text'] = ' '

		

	def update_cell(self, row, column):
		if not self.is_running:
			self.board.set(row, column, not self.board.get(row, column))
			if self.board.get(row, column):
				self.cells[row][column]['text'] = 'X'
			else:
				self.cells[row][column]['text'] = ' '

	def run(self):
		''' Run the app '''
		self.mainloop()



board = GameBoard(rows=16, columns=16)
app = GameOfLifeApp(tk.Tk(), board)
app.run()