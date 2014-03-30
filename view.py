from Tkinter import*
import classes_gui
import control_center
import tkMessageBox

class Main:
	def __init__(self, root):
		self.root = root
		self.cc = control_center.CC()
		self.root.geometry("200x90")
		self.root.title("CRS")
		self.root.resizable(width=FALSE, height=FALSE)
		self.createFrame()
		
	def createFrame(self):
		self.loginFrame = Frame(self.root)
		self.loginFrame.grid()
		Label(self.loginFrame, text="Course Registration System").grid(row=0, column=0, columnspan = 3)
		Label(self.loginFrame, text="Username: ").grid(row=1, column=0)
		self.username = Entry(self.loginFrame)
		self.username.grid(row=1, column=1, columnspan = 2)
		Label(self.loginFrame, text="Password: ").grid(row=2, column=0)
		self.password = Entry(self.loginFrame, show="*")
		self.password.grid(row=2, column=1, columnspan = 2)
		Button(self.loginFrame, text="Log-in", command=self.refresh).grid(row=3, column=0, ipadx=25, columnspan = 2)
		Button(self.loginFrame, text="Create", command=self.create).grid(row=3, column=2, ipadx=25)
		
	def refresh(self):
		self.getInput()
		self.createFrame()
	
	def getInput(self):
		try:
			self.input = {}
			self.input["Username"] = self.username.get()
			self.input["Password"] = self.password.get()
			login = self.cc.login(self.input)
			if login == True:
				tkMessageBox.showinfo("CRS", "Log-in successful!")
				self.loginFrame.destroy()
			else:
				raise Exception("Wrong userpass")
		except:
			tkMessageBox.showerror("CRS", "Wrong username/password")
	
	def create(self):
		user = Toplevel(self.root)
		createAccount = classes_gui.CreateAccount(user, self.cc)

root = Tk()
Main(root)
root.mainloop()