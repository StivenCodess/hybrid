import re
import sqlite3

class Model:
	def __init__(self):
		self.controller = None

	def set_controller(self, controller):
		self.controller = controller