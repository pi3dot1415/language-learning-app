import mysql.connector
from tkinter import *
import tkinter as tk
import time
import datetime

class Window (tk.Frame):
	
	def __init__ (self, root):
		tk.Frame.__init__(self, root)
		self.root=root
		self.set_user=None
		self.log_or_reg=True
		self.login_Page()
		
	def login_Page (self):
		if self.log_or_reg:
			self.clear_frame()
			self.log_or_reg=False
		
		self.var_login=StringVar()
		self.var_password=StringVar()
		
		self.login_text = Label(self.root, text="Type login")
		self.login_text.place(x=125, y=200, width=75, height=30)
		
		self.type_login = Entry(self.root, textvariable=self.var_login)
		self.type_login.place(x=225, y=200, width=150, height=30)
		
		self.password_text = Label(self.root, text="Type password")
		self.password_text.place(x=125, y=250, width=85, height=30)
		
		self.type_password = Entry(self.root, textvariable=self.var_password)
		self.type_password.place(x=225, y=250, width=150, height=30)
		
		self.login_button = Button(self.root, text='Login', command=lambda:self.authentication())
		self.login_button.place(x=250, y=300, width=100, height=30)
	
		self.redirect_text = Label(self.root, text="Don't have account yet?")
		self.redirect_text.place(x=225, y=400, width=150, height=30)
		
		self.redirect_to_registration = Button(self.root, text='Create an Account', command=lambda:self.register_Page())
		self.redirect_to_registration.place(x=225, y=450, width=150, height=30)
		
		self.btnq = Button(self.root, text='Quit', command=quit)
		self.btnq.place(x=450, y=450, width=100, height=30)
		
	def register_Page (self):
		if not self.log_or_reg:
			self.clear_frame()
			self.log_or_reg=True
		
		self.var_login_r=StringVar()
		self.var_password_r=StringVar()
		self.var_password_r2=StringVar()
		
		self.login_text = Label(self.root, text="Set login")
		self.login_text.place(x=125, y=150, width=75, height=30)
		
		self.type_login_r = Entry(self.root, textvariable=self.var_login_r)
		self.type_login_r.place(x=225, y=150, width=150, height=30)
		
		self.password_text = Label(self.root, text="Set password")
		self.password_text.place(x=125, y=200, width=85, height=30)
		
		self.type_password_r = Entry(self.root, textvariable=self.var_password_r)
		self.type_password_r.place(x=225, y=200, width=150, height=30)
		
		self.password_text = Label(self.root, text="Repeat password")
		self.password_text.place(x=125, y=250, width=95, height=30)
		
		self.repeat_password_r = Entry(self.root, textvariable=self.var_password_r2)
		self.repeat_password_r.place(x=225, y=250, width=150, height=30)
		
		self.login_button = Button(self.root, text='Register', command=lambda:self.registration())
		self.login_button.place(x=250, y=300, width=100, height=30)
	
		self.redirect_text = Label(self.root, text="Allready have account?")
		self.redirect_text.place(x=225, y=400, width=150, height=30)
		
		self.redirect_to_registration = Button(self.root, text='Login', command=lambda:self.login_Page())
		self.redirect_to_registration.place(x=225, y=450, width=150, height=30)
		
		self.btnq = Button(self.root, text='Quit', command=quit)
		self.btnq.place(x=450, y=450, width=100, height=30)
		
	def user_Page (self):
		self.redirect_text = Label(self.root, text=f"Showing user {self.set_user} page")
		self.redirect_text.place(x=200, y=350, width=200, height=30)
		
		self.btnq = Button(self.root, text='Sign Out', command=self.sign_out)
		self.btnq.place(x=450, y=50, width=100, height=30)
		
		self.btnq = Button(self.root, text='Quit', command=quit)
		self.btnq.place(x=450, y=450, width=100, height=30)
		
	def admin_page (self):
		pass
		
	def test_Page (self):
		pass
	
	def authentication(self):
		try:
			conn = mysql.connector.connect(
				host="127.0.0.1",
				user="user",
				database="pol_eng",
				password="password"
			)
		except:
			self.redirect_text = Label(self.root, text="Cannot connect")
			self.redirect_text.place(x=225, y=350, width=150, height=30)
			return None

		mycursor=conn.cursor()
		
		login=self.var_login.get()
		password=self.var_password.get()
		
		query = "SELECT password_ FROM users WHERE login LIKE '"+login+"';"
		mycursor.execute(query)
		
		password_=mycursor.fetchall()
		
		try:
			if password == password_[0]:
				self.set_user=login
				self.clear_frame()
				if login=="admin":
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
	
	def registration (self):
		try:
			conn = mysql.connector.connect(
				host="127.0.0.1",
				user="user",
				database="pol_eng",
				password="password"
			)
		except:
			self.redirect_text = Label(self.root, text="Cannot connect")
			self.redirect_text.place(x=225, y=350, width=150, height=30)
			return None

		mycursor=conn.cursor()
		
		login=self.var_login_r.get()
		password=self.var_password_r.get()
		password2=self.var_password_r2.get()
		
		query = "SELECT login FROM users WHERE login LIKE '"+login+"';"
		mycursor.execute(query)
		
		login_=mycursor.fetchall()
		
		try:
			if login == login_[0]:
				self.redirect_text = Label(self.root, text="Login is currently used")
				self.redirect_text.place(x=225, y=350, width=150, height=30)
		except:
			if password==password2 and len(password)>=8:
				subquery=str((login, password, str(datetime.datetime.today()).split()[0]))
				query = "INSERT INTO users (login, password_, join_date) VALUES "+subquery+";"
				#mycursor.execute(query)
				self.set_user=login
				self.clear_frame()
				if login=="admin":
					self.admin_page()
				else:
					self.user_Page()
			elif len(password)>=8:
				self.redirect_text = Label(self.root, text="Passwords don't match")
				self.redirect_text.place(x=225, y=350, width=150, height=30)
			else:
				self.redirect_text = Label(self.root, text="Password is too short")
				self.redirect_text.place(x=225, y=350, width=150, height=30)
		
		conn.close()
	
	def insert_words (self):
		pass

	def check_answer (self):
		pass
	
	def sign_out (self):
		self.set_user=None
		self.login_Page()
	
	def clear_frame(self):
		frame=Label(self.root, bg="lightgray")
		frame.place(x=0,y=0, width=600, height=600)

	def quit():
		import sys; sys.exit()

root=tk.Tk()
main = Window(root)
root.title('Fiszki')
root.wm_geometry('600x600')
root.mainloop()
