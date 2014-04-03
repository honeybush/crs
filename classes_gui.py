from Tkinter import*
import sys, traceback
import tkMessageBox

class BaseCRS:
	def __init__(self, user, cc):
		self.user = user
		self.cc = cc
		self.user.geometry("960x600")
		self.user.resizable(height=FALSE, width=FALSE)
		self.user.title("CRS")
		self.menu = Frame(self.user, width=960, height=30, bg="dark blue")
		self.menu.grid()
		self.content = Frame(self.user, width=960, height=570, bg="light green")
		self.content.grid(row=1, column=0)
		self.addButtons()
		self.changeContent()
	def addButtons(self):
		pass
	def changeContent(self):
		pass

class AdminPage(BaseCRS):
	def addButtons(self):
		Button(self.menu, text="Students List", command=self.students).pack(side=LEFT)
		Button(self.menu, text="Courses List", command=self.courses).pack(side=LEFT)
	def students(self):
		studentPage = StudentSearcher(self.content, self.cc)
	def courses(self):
		coursePage = CourseSearcher(self.content, self.cc)

class StudentPage(BaseCRS):
	def addButtons(self):
		Button(self.menu, text="Schedule", command=self.getSched, state=DISABLED).pack(side=LEFT)
		Button(self.menu, text="Grades").pack(side=LEFT)
		Button(self.menu, text="Enlist", command=self.enlist).pack(side=LEFT)
	def getSched(self):
		sched = Schedule(self.content, self.cc)
	def enlist(self):
		enlist = Enlister(self.content, self.cc)

class TeacherPage(BaseCRS):
	def addButtons(self):
		Button(self.menu, text="Schedule", state=DISABLED).pack(side=LEFT)
		Button(self.menu, text="Courses").pack(side=LEFT)

class Schedule:
	def __init__(self, contentPage, cc):
		self.content = contentPage
		self.cc = cc
		days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
		timeSlots = ("7-8:30", "8:30-10:00", "10:00-11:30", "11:30-1:00", "1:00-2:30", "2:30-4:00", "4:00-5:30", "5:30-7:00")
		schedule = {}
		perDay = {}
		temp = ""
		for d in days:
			for t in timeSlots:
				perDay[t] = temp
			schedule[d] = perDay
			perDay = {}
		schedule = self.addSched(schedule)
		self.drawSched(schedule)
	def addSched(self, schedule):
		schedule = self.cc.setSched(schedule)
		#print schedule
		return schedule
	def drawSched(self, schedule):
		f = Frame(self.content, width=960,height=570)
		f.pack()
		c = Canvas(f, width=960,height=570)
		c.pack()
		Label(c, text="Schedule").grid(row=0, column=0)
		schedays = schedule.keys()
		_x=2
		_y=0
		for i in schedays:
			temp = schedule.get(i)
			for j in temp:
				if _x == 2:
					if _y>0:
						Label(c, text=j).grid(row=_x, column=_y)
				elif _x>0:
					if _y == 0:
						Label(c, text=i).grid(row=_x, column=_y)
				_y+=1
			_y=0
			_x+=1
		_x = 3
		_y = 1
		for s in schedays:
			temp = schedule.get(s)
			for t in temp:
				Label(c, text=temp.get(t)).grid(row=_x, column=_y)
				_x+=1
			_x=2
			_y+=1

class Grades:
	def __init__(self):
		pass

class StudentSearcher:
	def __init__(self, contentPage, cc):
		self.content = contentPage
		self.cc = cc
		#self.createPage()
		self.addButtons()
	def createPage(self, names):
		self.addButtons()
		_y = 35
		for n in names:
			#print n
			Button(self.studentPage, text="View").place(x=10, y=_y)
			Label(self.studentPage, text=n).place(x=50, y=_y+2)
			_y+=25
	def addButtons(self):
		alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
		self.studentPage = Canvas(self.content, width=960, height=570)
		self.studentPage.grid()
		_x = 155
		for letter in alphabet:
			Button(self.studentPage, text=letter, command=lambda l=letter:self.getNames(l)).place(x=_x, y=5)
			_x+=25
	def getNames(self, letter):
		self.studentPage.destroy()
		#print letter
		names = self.cc.getStudentList(letter)
		#print names
		self.createPage(names)

class CourseSearcher:
	def __init__(self, contentPage, cc):
		self.content = contentPage
		self.cc = cc
		#self.createPage()
		self.addButtons()
		self.text = "View"
	def createPage(self, courses):
		self.addButtons()
		_y = 35
		for c in courses:
			#print c
			Button(self.coursePage, text=self.text).place(x=10, y=_y)
			Label(self.coursePage, text=c).place(x=50, y=_y+2)
			_y+=25
	def addButtons(self):
		alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
		self.coursePage = Canvas(self.content, width=960, height=570)
		self.coursePage.grid()
		_x = 100
		for letter in alphabet:
			Button(self.coursePage, text=letter, command=lambda l=letter:self.getCourse(l)).place(x=_x, y=5)
			_x+=25
		self.newcourse = Button(self.coursePage, text="New Course", command=self.newcourse)
		self.newcourse.place(x=_x+10, y=5)
	def newcourse(self):
		nc = NewCourse(self.coursePage, self.content, self.cc)
	def getCourse(self, letter):
		self.coursePage.destroy()
		#print letter
		course = self.cc.getCourseList(letter)
		#print course
		self.createPage(course)

class Enlister(CourseSearcher):
	def __init__(self, contentPage, cc):
		self.content = contentPage
		self.cc = cc
		#self.createPage()
		self.addButtons()
		self.text = "Enlist"
	def addButtons(self):
		alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
		self.coursePage = Canvas(self.content, width=960, height=570)
		self.coursePage.grid()
		_x = 100
		for letter in alphabet:
			Button(self.coursePage, text=letter, command=lambda l=letter:self.getCourse(l)).place(x=_x, y=5)
			_x+=25
	def createPage(self, courses):
		self.addButtons()
		_y = 35
		for c in courses:
			#print c
			Button(self.coursePage, text=self.text, command=lambda: self.enlist(c)).place(x=10, y=_y)
			Label(self.coursePage, text=c).place(x=50, y=_y+2)
			_y+=25
	def enlist(self, c):
		self.cc.enlist(c)

class NewCourse:
	def __init__(self, coursePage, content, cc):
		coursePage.destroy()
		self.content = content
		self.cc = cc
		self.nc = Canvas(self.content, width=960, height=570)
		self.nc.grid()
		self.pickedProf = ""
		labels = ("New Course", "Course: ", "Schedule (Day): ", "Schedule (Time): ", "Professor: ")
		_y = 10
		for l in labels:
			Label(self.nc, text=l).place(x=10, y=_y)
			_y+=30
		self.course = Entry(self.content)
		self.course.place(x=100, y=40)
		choices = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
		self.day = {}
		_x = 130
		for choice in choices:
			self.day[choice] = StringVar()
			pick = Checkbutton(self.nc, text=choice, variable=self.day[choice])
			pick.place(x=_x, y=70)
			_x+=70
			self.day[choice].set(0)
		timeSlots = ("7-8:30", "8:30-10:00", "10:00-11:30", "11:30-1:00", "1:00-2:30", "2:30-4:00", "4:00-5:30", "5:30-7:00")
		_x = 130
		self.type = StringVar()
		for time in timeSlots:
			#self.type[time] = IntVar()
			pick = Radiobutton(self.nc, text=time, variable=self.type, value=time)
			pick.place(x=_x, y=100)
			_x+=70
		self.type.set(0)
		Button(self.nc, text="Select", command=self.chooseProf).place(x=130, y=130)
		self.pp = Label(self.nc, text=self.pickedProf)
		self.pp.place(x=180, y=130)
		Button(self.nc, text="Submit", command=self.submit).place(x=10, y=160)
	def chooseProf(self):
		try:
			self.pickedProf = ""
			self.picprof = Toplevel(self.content, takefocus=True)
			self.picprof.geometry("200x350")
			self.f = Frame(self.picprof, width=200, height=350)
			self.f.grid(row=0, column=0)
			self.c = Canvas(self.picprof, scrollregion=(0, 0, 200, 350))
			self.s = Scrollbar(self.picprof, command=self.c.yview)
			self.s.grid(row=0, column=1, sticky="news")
			self.c["yscrollcommand"] = self.s.set
			self.c.create_window((0,0), window=self.f, anchor="nw")
			self.c.bind("<Configure>", self.resize)
			self.s.pack(side="right", fill="y")
			self.c.pack(side=LEFT, fill=BOTH)
			teacherList = self.cc.getTeacherList()
			self.tl = IntVar()
			_y = 5
		except:
			pass
		for teacher in teacherList:
			value = teacher
			teacher = Radiobutton(self.c, text=teacher, variable=self.tl, value=teacher, command=lambda a=teacher:self.getVal(a))
			teacher.place(x=5, y=_y)
			_y+=30
		Button(self.c, text="Submit", command=self.submitProf).place(x=5, y=_y)
	def getVal(self, teacher):
		self.pickedProf = ""
		#print teacher, self.pickedProf
		self.pickedProf = teacher
	def resize(self, e):
		self.c.itemconfig(self.f, width=200, height=350)
	def submitProf(self):
		self.pp.configure(text=self.pickedProf)
		self.picprof.destroy()
	def submit(self):
		try:
			courseInfo = {}
			courseInfo["course"] = self.course.get()
			courseInfo["prof"] = self.pickedProf
			temp = []
			for i in self.day.keys():
				temp2 = self.day.get(i)
				temp3 = temp2.get()
				if temp3 == 1 or temp3 == "1":
					temp.append(i)
			#print temp
			courseInfo["day slot"] = temp
			courseInfo["time slot"] = self.type.get()
			self.cc.createCourse(courseInfo)
			self.content.destroy()
		except:
			tkMessageBox.showerror("Incorrect Info", "Please double check your fields")
			traceback.print_exc(file=sys.stdout)
		

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
				newUser = self.cc.createUser(self.userinfo)
				tkMessageBox.showinfo("Create Account", "Successful! your username is "+newUser.username)
				self.user.destroy()
		except:
			tkMessageBox.showerror("Incorrect Info", "Please double check your fields")
			traceback.print_exc(file=sys.stdout)