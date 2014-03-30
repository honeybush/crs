class User:
	def __init__(self, userInfo):
		self.userInfo = userInfo
		self.fn = ""
		self.mi = ""
		self.ln = ""
		self.type = ""
		self.password = ""
		self.setDetails()
		self.username = self.convertName()
	def setDetails(self):
		self.fn = self.userInfo.get("first name")
		self.mi = self.userInfo.get("middle initial")
		self.ln = self.userInfo.get("last name")
		self.password = str(self.userInfo.get("password"))
	def giveName(self):
		return mi+",", fn, mi
	def giveType(self):
		return type
	def convertName(self):
		username = self.fn[0]+self.mi+self.ln
		username = username.lower()
		if self.searchUsername == False:
			return username
		else:
			n = self.usernameCount(username)
			return username+str(n+1)
	def searchUsername(self, username):
		userlist = self.getUsers()
		for users in userlist:
			if users[len(username)-1] == username:
				return True
		return False
	def usernameCount(self, username):
		userlist = self.getUsers()
		n = 0
		for users in userlist:
			if users[len(username)-1] == username:
				n+=1
		return n
	def getUsers(self):
		f = open("userlist.txt")
		users = []
		for line in f:
			if not(line[0] == "\t"):
				temp = line.split(":")
				users.append(temp)
		f.close
		return users

class Teacher(User):
	def __init__(self, userInfo):
		self.userInfo = userInfo
		self.fn = ""
		self.mi = ""
		self.ln = ""
		self.type = "teacher"
		self.courses = []
		self.setDetails()
		self.username = self.convertName()
	def getCourses(self, courses):
		self.courses = courses
	def giveCourse(self):
		return self.courses

class Student(User):
	def __init__(self, userInfo):
		self.userInfo = userInfo
		self.fn = ""
		self.mi = ""
		self.ln = ""
		self.type = "student"
		self.courses = []
		self.setDetails()
		self.username = self.convertName()
	def getCourses(self, courses):
		self.courses = courses
	def giveCourse(self):
		return self.courses

class Admin(User):
	def __init__(self, userInfo):
		self.userInfo = userInfo
		self.fn = ""
		self.mi = ""
		self.ln = ""
		self.type = "admin"
		self.courses = []
		self.setDetails()
		self.username = self.convertName()