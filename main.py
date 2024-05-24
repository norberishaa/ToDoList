import ttkbootstrap as tb
from tkinter import font as tkfont


class ToDoList:
	def __init__(self, root):
		self.root = root
		self.root.title('ToDoList')
		self.root.geometry('700x1080+610+0')

		self.todo_list = []
		self.textbox = None

		self.top()

	def top(self):

		# FRAME 1
		frame_one = tb.Frame(self.root, style='primary')

		main_label_font = tkfont.Font(family='Helvetica', size=30, weight='bold')
		main_label = tb.Label(frame_one, font=main_label_font, text='TO DO LIST ', style='primary-inverse')
		main_label.pack(pady=10)

		self.textbox = tb.Entry(frame_one, font=('Helvetica', 12), width=60, style='dark')
		self.textbox.bind('<Return>', self.list)
		self.textbox.pack(side='left', padx=20, pady=10)

		add_button = tb.Button(frame_one, text='+', style='dark', width=150, command=self.list, takefocus=False)
		add_button.pack(side='right', padx=20)

		frame_one.pack(fill='x')

	@staticmethod
	def change_label_style(item_frame, var, seperator):
		if var.get() == 1:
			item_frame.destroy()
			seperator.destroy()

	def button(self, item_f rame, seperator):
		var = tb.IntVar()
		check_button = tb.Checkbutton(item_frame, variable=var, onvalue=1, offvalue=0, command=lambda: self.change_label_style(item_frame, var, seperator))
		check_button.pack(side='right')

	def list(self, event=None):
		item = self.textbox.get()

		if len(item) > 0:
			self.textbox.delete(0, 'end')

			item_frame = tb.Frame(self.root)

			new_label = tb.Label(item_frame, style='default', text=item, font=('Helvetica', 15))
			new_label.pack(side='left')
			self.todo_list.append(new_label)

			item_frame.pack(fill='x')

			seperator = tb.Separator(self.root, orient='horizontal')
			seperator.pack(fill='x', pady=10)

			self.button(item_frame, seperator)


if __name__ == "__main__":
	root_window = tb.Window(themename='darkly')
	app = ToDoList(root_window)
	root_window.mainloop()
