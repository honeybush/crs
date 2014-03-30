from Tkinter import*
import sys, traceback
import tkMessageBox

class CreateAccount:
	def __init__(self, user, cc):
		self.user = user
		self.cc = cc
		self.user.geometry("373x150")
		self.user.resizable(height=FALSE, width=FALSE)
		self.user.title("CRS")
		self.create = Frame(self.user)
		self.create.grid()
		Label(self.create, text="New Account:").grid(columnspan=3)
		self.fn = Entry(self.create)
		self.mi = Entry(self.create, width=1)
		self.ln = Entry(self.create)
		self.fn.grid(row=1, column=0)
		self.mi.grid(row=1, column=1)
		self.ln.grid(row=1, column=2)
		Label(self.create, text="First Name").grid(row=2, column=0)
		Label(self.create, text="Middle Initial").grid(row=2, column=1)
		Label(self.create, text="Last Name").grid(row=2, column=2)
		choices = ["student", "teacher", "admin"]
		self.type = IntVar()
		x = 1
		for choice in choices:
			pick = Radiobutton(self.create, text=choice, variable=self.type, value=x)
			pick.grid(row=3, column=x-1)
			x = x+1
		Label(self.create, text="Password: ").grid(row=4, column=0)
		self.password = Entry(self.create, show="*")
		self.password.grid(row=4, column=1)
		Button(self.create, text="Submit", command=self.submit).grid(row=5, column=1)
	def submit(self):
		try:
			self.userinfo = {}
			self.userinfo["first name"] = self.fn.get()
			self.userinfo["middle initial"] = self.mi.get()
			self.userinfo["last name"] = self.ln.get()
			self.userinfo["type"] = self.type.get()
			self.userinfo["password"] = self.password.get()
			answer = tkMessageBox.askyesno("Caution!", "Are you sure with your answers?")
			if answer == True:
				self.cc.createUser(self.userinfo)
				tkMessageBox.showinfo("Create Account", "Successful!")
				self.user.destroy()
		except:
			tkMessageBox.showerror("Incorrect Info", "Please double check your fields")
			traceback.print_exc(file=sys.stdout)