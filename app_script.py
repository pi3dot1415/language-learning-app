import mysql.connector
from tkinter import *
import tkinter as tk
import time
import datetime
import random

class Window (tk.Frame):
	
	def __init__ (self, root):
		tk.Frame.__init__(self, root)
		self.root=root
		self.set_user=None
		self.log_or_reg=True
		self.during_test=False
		self.conn_host="127.0.0.1"
		self.conn_user="username"
		self.conn_database="pol_eng"
		self.conn_password="password"
		self.language="English"
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
		
		self.btnq = Button(self.root, text='Quit', command=self.quit)
		self.btnq.place(x=450, y=450, width=100, height=30)
		
	def user_Page (self):
		if self.during_test:
			self.clear_frame()
			self.during_test=False
		
		self.redirect_text = Label(self.root, text=f"Showing user {self.set_user} page")
		self.redirect_text.place(x=200, y=350, width=200, height=30)
		
		self.btns = Button(self.root, text='Sign Out', command=self.sign_out)
		self.btns.place(x=450, y=50, width=100, height=30)
		
		self.start_test_e2p = Button (self.root, text='ENG to POL', command=lambda: self.test_Page(language="English"))
		self.start_test_e2p.place(x=250, y=150, width=100, height=30)
		
		self.start_test_p2e = Button (self.root, text='POL to ENG', command=lambda: self.sign_out(language="Polish"))
		self.start_test_p2e.place(x=250, y=200, width=100, height=30)
		
		self.btnq = Button(self.root, text='Quit', command=quit)
		self.btnq.place(x=450, y=450, width=100, height=30)
		
	def admin_page (self):
		pass
		
	def test_Page (self, language=self.language):
		self.language=language
		if not self.during_test:
			self.clear_frame()
			self.during_test=True
	
		self.btns = Button(self.root, text='Sign Out', command=self.sign_out)
		self.btns.place(x=450, y=50, width=100, height=30)
		
		self.btns = Button(self.root, text='Main Page', command=self.user_Page)
		self.btns.place(x=450, y=150, width=100, height=30)
		
		self.btnq = Button(self.root, text='Quit', command=quit)
		self.btnq.place(x=450, y=450, width=100, height=30)
		
		try:
			conn = mysql.connector.connect(
				host=self.conn_host,
				user=self.conn_user,
				database=self.conn_database,
				password=self.conn_password
			)
		except:
			self.redirect_text = Label(self.root, text="Cannot connect")
			self.redirect_text.place(x=225, y=350, width=150, height=30)
			return None

		mycursor=conn.cursor()
		
		query = "SELECT * FROM(SELECT polish_word, english_word, COUNT(is_correct) AS 'ans' FROM dictionary RIGHT JOIN answers ON dictionary.id=answers.word_id UNION SELECT polish_word, english_word, 0 AS 'ans' FROM dictionary) AS dft GROUP BY polish_word ORDER BY ans ASC;"
		
		mycursor.execute(query)
		
		words_table=mycursor.fetchall()
		population=[]
		words=[]
		
		for row in words_table:
			population.append(row[i][2])
			words.append(row[i][:2])
		
		question=random.choices(words, weights=population, k=1)
		
		if language=="Polish":
			self.text_label = Label(self.root, text=question[0])
			answ=1
		elif language=="English":
			self.text_label = Label(self.root, text=question[1])
			answ=0
		self.text_label.place(x=200, y=250, width=200, height=30)
		
		self.check_ans = Button(self.root, text="Check Answer", command=lambda:self.check_answer(question[answ]))
		self.check_ans.place(x=225, y=300, width=150, height=30)
		
		self.next_qst = Button(self.root, text="Next question", command=self.next_question)
		self.next_qst.place(x=225, y=400, width=150, height=30)
		
	def authentication(self):
		try:
			conn = mysql.connector.connect(
				host=self.conn_host,
				user=self.conn_user,
				database=self.conn_database,
				password=self.conn_password
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
				host=self.conn_host,
				user=self.conn_user,
				database=self.conn_database,
				password=self.conn_password
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

	def next_question (self):
		#insert into answers table
		conn.close()
		test_Page()

	def check_answer (self, answr):
		self.text_label = Label(self.root, text=answr)
		self.text_label.place(x=200, y=350, width=200, height=30)
		
		#insert into answers table
		
		self.next_qst = Button(self.root, text="Next question", command=self.next_question)
		self.next_qst.place(x=225, y=400, width=150, height=30)
		
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
#root.protocol("WM_DELETE_WINDOW", lambda: root.quit())
root.mainloop()
