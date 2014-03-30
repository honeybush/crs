import classes_users

class Factory:
	def createUser(self, userInfo):
		self.userInfo = userInfo
		type = self.userInfo.get("type")
		if type == 1:
			self.user = classes_users.Student(userInfo)
		elif type == 2:
			self.user = classes_users.Teacher(userInfo)
		else:
			self.user = classes_users.Admin(userInfo)
		return self.user