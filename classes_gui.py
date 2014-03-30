from Tkinter import*

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
		self.mi = Entry(self.create)
		self.ln = Entry(self.create)
		self.fn.grid(row=1, column=0)
		self.mi.grid(row=1, column=1)
		self.ln.grid(row=1, column=2)
		Label(self.create, text="First Name").grid(row=2, column=0, padx=10)
		Label(self.create, text="Middle Initial").grid(row=2, column=1, padx=10)
		Label(self.create, text="Last Name").grid(row=2, column=2, padx=10)
		choices = ["student", "teacher", "admin"]
		self.type = StringVar()
		self.type.set(choices[0])
		x = 0
		for choice in choices:
			pick = Radiobutton(self.create, text=choice, variable=self.type, value=x)
			pick.grid(row=3, column=x)
			x+=1
		Label(self.create, text="Password: ").grid(row=4, column=0)
		self.password = Entry(self.create, show="*")
		self.password.grid(row=4, column=1)
		Button(self.create, text="Submit", command=self.submit).grid(row=5, column=1)
	def submit(self):
		print type
		self.userinfo = {}
		self.userinfo["first name"] = self.fn.get()
		self.userinfo["middle initial"] = self.mi.get()
		self.userinfo["last name"] = self.ln.get()
		self.userinfo["type"] = self.type.get()
		self.userinfo["password"] = self.password.get()
		self.cc.createUser(self.userinfo)