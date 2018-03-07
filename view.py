import tkinter as tk
import GameBoard

class GameOfLifeApp(tk.Frame):
   
		# Initialize window using the parent's constructor
		tk.Frame.__init__(self,
						  master,
						  width=500,
						  height=500)
		self.model = board

		# Set the title
		self.master.title('Game Of Life')
 
		# This allows the size specification to take effect
		self.pack_propagate(0)
 
		# We'll use the flexible pack layout manager
		self.pack()

		# The greeting selector
		# Use a StringVar to access the selector's value
		self.greeting_var = tk.StringVar()
		self.greeting = tk.OptionMenu(self,
									  self.greeting_var,
									  'rows: ' + str(self.model.rows),
									  'goodbye',
									  'heyo')
		self.greeting_var.set('hello')
 
		# The recipient text entry control and its StringVar
		self.recipient_var = tk.StringVar()
		self.recipient = tk.Entry(self,
								  textvariable=self.recipient_var)
		self.recipient_varset('world')
 
		# The go button
		self.go_button = tk.Button(self,
								   text='Go',
								   command=self.print_out)
 
		# Put the controls on the form
		self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
		self.greeting.pack(fill=tk.X, side=tk.TOP)
		self.recipient.pack(fill=tk.X, side=tk.TOP)
 
	def print_out(self):
		#Print a greeting constructed
		#	from the selections made by
		#	the user. 
		print('%s, %s!' % (self.greeting_var.get().title(),
						   self.recipient_var.get()))

	def resize(self):
	  # get new rows 
	  # get new columns
	  # create new data model 
	  # update view

	def clear(self):
	  # clear all living cells

	def increment(self):
	  # update model
	  # update view

	def start_stop_game(self):
	  # determine if game is running

	  # if running set event to stop, set game to running = False

	  # if not running set event to start, set game to running = True



	def run(self):
		''' Run the app '''
		self.mainloop()
 

board = GameBoard.GameBoard()

app = GameOfLifeApp(tk.Tk(), board)
app.run()