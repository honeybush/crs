import classes_users
import classes_obj

class Factory:
	def createUser(self, userInfo):
		self.userInfo = userInfo
		#print self.userInfo.get("type") + "-"
		type = self.userInfo.get("type")
		if type == 1 or type == "student":
			#print "1"
			self.user = classes_users.Student(userInfo)
		elif type == 2 or type == "teacher":
			#print "2"
			self.user = classes_users.Teacher(userInfo)
		else:
			#print "3"
			self.user = classes_users.Admin(userInfo)
		return self.user
	def createCourse(self, courseInfo):
		self.courseInfo = courseInfo
		course = classes_obj.Course(courseInfo)
		return course