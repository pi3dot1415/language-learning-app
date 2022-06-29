import mysql.connector
from tkinter import *
import tkinter as tk
import time
import datetime

class Window (tk.Frame):
	
	def __init__ (self, root):
		tk.Frame.__init__(self, root)
		self.root=root
		self.login_Page()
		self.set_user=None
		
	def login_Page (self):
		self.var_login=StringVar()
		self.var_password=StringVar()
		
		self.type_login = Entry(self.root, textvariable=self.var_login)
		self.type_login.place(x=225, y=200, width=150, height=30)
		
		self.type_password = Entry(self.root, textvariable=self.var_password)
		self.type_password.place(x=225, y=250, width=150, height=30)
		
		self.login_button = Button(self.root, text='Login', command=lambda:self.authentication())
		self.login_button.place(x=250, y=300, width=100, height=30)
	
		self.redirect_text = Label(self.root, text="Don't have account yet?")
		self.redirect_text.place(x=225, y=400, width=150, height=30)
		
		self.redirect_to_registration = Button(self.root, text='Create an Account', command=lambda:self.register_Page())
		self.redirect_to_registration.place(x=225, y=450, width=150, height=30)
		
	def register_Page (self):
		pass
		
	def user_Page (self):
		pass
		
	def admin_page (self):
		pass
		
	def test_Page (self):
		pass
	
	def authentication(self):
		try:
			conn = mysql.connector.connect(
				host="127.0.0.1",
				user="username", 
				database="pol_eng",
				password="password"
			)
			print("Succes")
		except:
			print("Connection failed")
			return None

		mycursor=conn.cursor()
		
		#TODO: geting password and login
		login="0"
		password="N"
		
		query = "SELECT password_ FROM users WHERE login LIKE '"+login+"';"
		mycursor.execute(query)
		
		password_=mycursor.fetchall()
		
		try:
			if password == password_[0]:
				self.set_user=login
				if login="admin"
					self.admin_page()
				else:
					self.user_Page()
			else:
				self.redirect_text = Label(self.root, text="Wrong password")
				self.redirect_text.place(x=225, y=350, width=150, height=30)
		except:
			self.redirect_text = Label(self.root, text="Wrong login")
			self.redirect_text.place(x=225, y=350, width=150, height=30)
		
		conn.close()
	
	def insert_words (self):
		pass

	def check_answer (self):
		pass

	def quit():
		import sys; sys.exit()

root=tk.Tk()
main = Window(root)
root.title('Fiszki')
root.wm_geometry('600x600')
root.mainloop()
