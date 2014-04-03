import factory

class CC:
	def __init__(self):
		self.username = ""
		self.factory = factory.Factory()
		self.userlist = {}
		self.userlist2 = []
		self.courselist = []
		self.studentlist = {}
	def createUser(self, userInfo):
		newUser = self.factory.createUser(userInfo)
		self.inputUser(newUser)
		return newUser
	def getUserList(self):
		userlist = self.getUsers()
		self.userlist = userlist
	def getUserList2(self):
		self.getUserList()
		self.userlist2 = []
		userlist = self.userlist.keys()
		#print self.userlist.keys()
		for u in userlist:
			userInfo = self.userlist.get(u)
			#print userInfo.get("type")
			user = self.factory.createUser(userInfo)
			#print user.type
			self.userlist2.append(user)
	def getStudentList(self, letter):
		self.getUserList2()
		namelist = []
		namelist_f = []
		for u in self.userlist2:
			#print u.type
			if u.type == "student":
				namelist.append(u.fullname)
				#print u.username
				#print u.fullname
		namelist = sorted(namelist)
		#print namelist
		for n in namelist:
			if n[0] == letter:
				namelist_f.append(n)
		return namelist_f
	def getTeacherList(self):
		self.getUserList2()
		namelist = []
		for u in self.userlist2:
			#print u.type
			if u.type == "teacher":
				namelist.append(u.fullname)
				#print u.username
				#print u.fullname
		namelist = sorted(namelist)
		#print namelist
		return namelist
	def searchUser(self, username):
		self.getUserList()
		for users in self.userlist.keys():
			if users == username:
				return True
		return False
	def confirmPass(self, username, password):
		#print self.userlist.get(username)
		userInfo = self.userlist.get(username)
		if userInfo.get("password") == password:
			return True
		else:
			return False
	def login(self, loginfo):
		self.username = loginfo.get("username")
		password = loginfo.get("password")
		temp_1 = self.searchUser(self.username)
		temp_2 = self.confirmPass(self.username, password)
		#print temp_1, temp_2, password
		if temp_1 == temp_2 == True:
			return True
		else:
			return False
	def getTypeLog(self, loginfo):
		username = loginfo.get("username")
		self.getUserList()
		user = self.userlist.get(username)
		type = user.get("type")
		return type
	def inputUser(self, user):
		f = open("userlist.txt", "a")
		temp = user.username+":"+user.password+"\n"
		f.write(temp)
		temp = "\t"+user.ln+", "+user.fn+" "+user.mi+"\n"
		f.write(temp)
		temp = "\t"+user.type+"\n"
		f.write(temp)
		f.close()
	def getUsers(self):
		f = open("userlist.txt", "r")
		users = {}
		userInfo = {}
		currUser = ""
		types = ("student", "teacher", "admin")
		temp3 = ("Courses")
		for line in f:
			#print line
			if line[0] == "\t":
				line = line[1:]
				if any(s in line for s in types):
					#print currUser, line
					userInfo = users.get(currUser)
					userInfo["type"] = line[:len(line)-1].rstrip()
				#elif any(s in line for s in temp3):
				#	userInfo = users.get(currUser)
				#	temp = line.split(":")
				#	userInfo["Courses"] = temp
				else:
					userInfo = users.get(currUser)
					temp = line.split()
					temp2 = temp[0]
					temp[0] = temp2[:len(temp2)-1]
					userInfo["last name"] = temp[0]
					userInfo["middle initial"] = temp[len(temp)-1].rstrip()
					temp2 = ""
					for n in range(1, len(temp)-1):
						temp2 = temp2+temp[n]+" "
					userInfo["first name"] = temp2[:len(temp2)-1]
			else:
				temp = line.split(":")
				userInfo["password"] = temp[1].rstrip()
				currUser = temp[0]
				userInfo["username"] = currUser
				users[currUser] = userInfo
			userInfo = {}
		f.close
		#print users
		return users
	def createCourse(self, courseInfo):
		newCourse = self.factory.createCourse(courseInfo)
		self.inputCourse(newCourse)
	def inputCourse(self, course):
		#print course.daySlot
		temp = ""
		for d in course.daySlot:
			temp = temp+","+d
		temp = temp[1:]
		f = open("courselist.txt", "a")
		f.write(course.section+" "+temp.lower()+" "+course.timeSlot+"\n")
		f.write("\t"+"C:"+course.course+"\n")
		f.write("\t"+"P:"+course.prof+"\n")
		f.close()
	def inputCourse2(self, course):
		self.inputCourse(course)
		f = open("courselist.txt", "a")
		for student in course.students:
			f.write("\t"+student+"\n")
		f.close
	def setSched(self, schedule):
		return schedule
	def getStudentFile(self):
		studentList = {}
		grades = {}
		currstud = ""
		f = open("studentgradelist.txt", "r")
		for line in lines:
			if line[0] == "\t":
				grades = studentList.get(currstud)
				temp = line.split()
				grades[temp[0]] = temp[1].rstrip()
			else:
				currstud = line.rstrip()
				studentList[currstud] = grades
		f.close()
		return studentList
	def getStudentGradeList(self):
		studentList = self.getStudentFile()
		students = {}
		self.getUserList2()
		for u in self.userlist2:
			#print u.type
			if u.type == "student":
				students[u.fullname] = u
		for s in studentList.keys():
			temp = students.get(s)
			temp2 = studentList.get(s)
			temp.courses = temp2
			students[s] = temp
		self.studentlist = students
	def getCourseFile(self):
		courseList = {}
		courseInfo = {}
		students = {}
		f = open("courselist.txt", "r")
		for lines in f:
			lines = lines.rstrip()
			if lines[0] == "\t":
				courseInfo = courseList.get(currcourse)
				lines = lines[1:]
				if lines[0:2] == "C:":
					lines = lines[2:]
					courseInfo["course"] = lines
				elif lines[0:2] == "P:":
					lines = lines[2:]
					courseInfo["prof"] = lines
				else:
					temp = lines.split(":")
					student = temp[0]
					grade = temp[1].rstrip()
					students[student] = grade
			else:
				temp = lines.split()
				currcourse = temp[0]
				temp2 = temp[1].split(",")
				courseInfo["section"] = temp[0]
				courseInfo["day slot"] = temp2
				courseInfo["time slot"] = temp[2]
				courseList[currcourse] = courseInfo
			courseInfo = {}
		f.close()
		return courseList
	def getCourses(self):
		courseList = self.getCourseFile()
		#print courseList
		self.courselist = []
		for course in courseList:	
			c = self.factory.createCourse(courseList.get(course))
			self.courselist.append(c)
			#print c.section
		return self.courselist
	def getCourseList(self, letter):
		courselist = self.getCourses()
		courses = []
		for c in courselist:
			#print c.section
			if c.section[0] == letter.lower():
				courses.append(c.section)
		return courses
	def enlist(self, course):
		courselist = self.getCourses()
		self.getUserList2()
		for c in courselist:
			if c.section == course:
				c.students.append(self.username)
		for u in self.userlist2:
			if u.username == self.username:
				u.courses[course] = " "
		open("courselist.txt", "w").close()
		for c in courselist:
			self.inputCourse2(c)
		open("studentgradelist.txt", "w").close()
		for user in self.userlist2:
			self.inputStudentGrades(user)
	def inputStudentGrades(self, user):
		f = open("studentgradelist.txt", "a")
		print user.courses
		f.write(user.fullname+"\n")
		for u in user.courses.keys():
			f.write("\t"+u+" "+user.courses.get(u))
		f.close()
#test = CC()
#test.getUsers()