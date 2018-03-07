import tkinter as tk
from GameBoard import GameBoard
class GameOfLifeApp(tk.Frame):
	''' An example application for TkInter.  Instantiate
		and call the run method to run. '''
	def __init__(self, master, board):
		# Initialize window using the parent's constructor
		tk.Frame.__init__(self,
						  master,
						  width=300,
						  height=200)
		# set data model
		self.board = board

		# Set the title
		self.master.title('TkInter Example')
 
		# This allows the size specification to take effect
		self.pack_propagate(0)
 
		# We'll use the flexible pack layout manager
		self.pack()
 
		# The greeting selector
		# Use a StringVar to access the selector's value
		self.greeting_var = tk.StringVar()
		self.greeting = tk.OptionMenu(self,
									  self.greeting_var,
									  'hello',
									  'goodbye',
									  'heyo')
		self.greeting_var.set('hello')
 
		# The recipient text entry control and its StringVar
		self.recipient_var = tk.StringVar()
		self.recipient = tk.Entry(self,
								  textvariable=self.recipient_var)
		self.recipient_var.set('world')
 
		# The go button
		self.go_button = tk.Button(self,
								   text='Go',
								   command=self.print_out)
 
		# Put the controls on the form
		self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
		self.greeting.pack(fill=tk.X, side=tk.TOP)
		self.recipient.pack(fill=tk.X, side=tk.TOP)
 
	def print_out(self):
		''' Print a greeting constructed
			from the selections made by
			the user. '''
		print('%s, %s!' % (self.greeting_var.get().title(),
						   self.recipient_var.get()))


	def resize(self):
		print()
		# get new row/col size 
		# create new data model
		# update view

	def clear(self):
		print()
		# clear data model
		# update view

	def iterate_game(self):
		print()
		# update data model
		# update view

	def start_stop_game(self):
		print()
		# determine if game is running
		# if running, set event to stop, set running = false
		# if not running, set event to start, set running  = true

	def update_view(self):
		print()
		# update board representation 
		# update start-stop game button

	def run(self):
		''' Run the app '''
		self.mainloop()

board = GameBoard()
app = GameOfLifeApp(tk.Tk(), board)
app.run()