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
		self.correct=""
		self.conn_host="127.0.0.1"
		self.conn_user="Username"
		self.conn_database="pol_eng"
		self.conn_password="Password"
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
		
		self.btnq = Button(self.root, text='Quit', command=quit)
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
		
		self.start_test_p2e = Button (self.root, text='POL to ENG', command=lambda: self.test_Page(language="Polish"))
		self.start_test_p2e.place(x=250, y=200, width=100, height=30)
		
		self.btnq = Button(self.root, text='Quit', command=quit)
		self.btnq.place(x=450, y=450, width=100, height=30)
		
	def admin_page (self):
		if not self.during_test:
			self.clear_frame()
			self.during_test=True
		
		self.var_english=StringVar()
		self.var_polish=StringVar()
		
		self.btns = Button(self.root, text='Sign Out', command=self.sign_out)
		self.btns.place(x=450, y=50, width=100, height=30)
		
		self.btnq = Button(self.root, text='Quit', command=quit)
		self.btnq.place(x=450, y=450, width=100, height=30)
		
		self.text_label = Label(self.root, text='Insert polish word')
		self.text_label.place(x=200, y=200, width=200, height=30)
		
		self.type_pol = Entry(self.root, textvariable=self.var_polish)
		self.type_pol.place(x=225, y=250, width=150, height=30)
		
		self.text_label = Label(self.root, text='Insert english word')
		self.text_label.place(x=200, y=300, width=200, height=30)
		
		self.type_eng = Entry(self.root, textvariable=self.var_english)
		self.type_eng.place(x=225, y=350, width=150, height=30)
		
		self.inst_words = Button(self.root, text="Insert words", command=self.insert_words)
		self.inst_words.place(x=225, y=400, width=150, height=30)
				
	def test_Page (self, language=False):
		if language:
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
		
		query = "SELECT * FROM(SELECT dictionary.id, polish_word, english_word, COUNT(is_correct) AS 'ans' FROM dictionary RIGHT JOIN answers ON dictionary.id=answers.word_id UNION SELECT dictionary.id, polish_word, english_word, 0 AS 'ans' FROM dictionary) AS dft GROUP BY polish_word ORDER BY ans ASC;"
		
		mycursor.execute(query)
		
		words_table=mycursor.fetchall()
		population=[]
		words=[]
		
		for row in words_table:
			if row != (None, None, 0):
				population.append(row[3])
				words.append(row[:3])
		m=max(population)
		
		for i in range(len(words)):
			population[i]=m+1-population[i]
		
		question=random.choices(words, weights=population, k=1)
		if self.language=="Polish":
			self.text_label = Label(self.root, text=question[0][1])
			answ=2
		elif self.language=="English":
			self.text_label = Label(self.root, text=question[0][2])
			answ=1
		self.text_label.place(x=200, y=250, width=200, height=30)
		
		self.var_answer=StringVar()
		
		self.print_answer = Entry(self.root, textvariable=self.var_answer)
		self.print_answer.place(x=225, y=300, width=150, height=30)
		
		self.check_ans = Button(self.root, text="Check Answer", command=lambda:self.check_answer(question,answ))
		self.check_ans.place(x=225, y=350, width=150, height=30)
		
		self.next_qst = Button(self.root, text="Next question", command=lambda:self.next_question(question,answ))
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
		
		query = "SELECT id, login, password_ FROM users WHERE login LIKE '"+login+"';"
		mycursor.execute(query)
		
		password_=mycursor.fetchall()
		
		try:
			if password_[0][1]!=login:
				self.redirect_text = Label(self.root, text="Wrong login")
				self.redirect_text.place(x=225, y=350, width=150, height=30)
				return None
			self.user_id=password_[0][0]
			if password == password_[0][2]:
				self.set_user=login
				self.clear_frame()
				if login.lower()=="admin":
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
		
		query = "SELECT id, login FROM users WHERE login LIKE '"+login+"';"
		mycursor.execute(query)
		
		login_=mycursor.fetchall()
		self.user_id=login[0][0]
		
		try:
			if login == login_[0][1]:
				self.redirect_text = Label(self.root, text="Login is currently used")
				self.redirect_text.place(x=225, y=350, width=150, height=30)
		except:
			if password==password2 and len(password)>=8:
				subquery=str((login, password, str(datetime.datetime.today()).split()[0]))
				query = "INSERT INTO users (login, password_, join_date) VALUES "+subquery+";"
				mycursor.execute(query)
				conn.commit()
				self.set_user=login
				self.clear_frame()
				if login.lower()=="admin":
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
		
		word_pl=self.var_polish.get()
		word_en=self.var_english.get()
		
		if word_en =="" or word_pl=="":
			conn.close()
			return None
		
		subquery=str((word_pl,word_en))
		query = "INSERT INTO dictionary(polish_word, english_word) VALUES"+subquery+";"
		
		mycursor.execute(query)
		conn.commit()
		
		conn.close()
		
		self.during_test=False
		self.admin_page()

	def next_question (self, question, answ, is_correct=None):
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
		
		if is_correct==None:
			if question[0][answ].lower()==self.var_answer.get():
				is_correct="Correct"
			elif self.var_answer.get()=="":
				is_correct="Skipped"
			else:
				is_correct="Wrong"
		
		if answ==1:
			language_="POL"
		else:
			language_="ENG"
		
		mycursor=conn.cursor()
		
		subquery=str((self.user_id, question[0][0], language_, is_correct, str(datetime.datetime.today()).split()[0]))
		query = "INSERT INTO answers(user_id, word_id, word_language, is_correct, answer_date) VALUES"+subquery+";"
		
		print(query)
		mycursor.execute(query)
		conn.commit()
		
		conn.close()
		self.during_test=False
		self.test_Page()

	def check_answer (self, question, answ):
		self.text_label = Label(self.root, text="Your answer: "+self.var_answer.get())
		self.text_label.place(x=200, y=300, width=200, height=30)
	
		self.text_label = Label(self.root, text="Correct answer: "+question[0][answ])
		self.text_label.place(x=200, y=350, width=200, height=30)
		
		if question[0][answ].lower()==self.var_answer.get():
			is_correct="Correct"
		else:
			is_correct="Wrong"
		
		self.next_qst = Button(self.root, text="Next question", command=lambda:self.next_question(question, answ, is_correct))
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
root.mainloop()
