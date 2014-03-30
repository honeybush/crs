import factory

class CC:
	def __init__(self):
		self.factory = factory.Factory()
		self.userlist = {}
	def createUser(self, userInfo):
		self.newUser = self.factory.createUser(userInfo)
		self.inputUser(self.newUser)
		self.newUser.reset()
	def getUserList(self):
		userlist = self.getUsers()
		self.userlist = userlist
	def searchUser(self, username):
		self.getUserList()
		for users in self.userlist.keys():
			if users == username:
				return True
		return False
	def confirmPass(self, username, password):
		#print self.userlist.get(username)
		if self.userlist.get(username) == password:
			return True
		else:
			return False
	def login(self, loginfo):
		username = loginfo.get("Username")
		password = loginfo.get("Password")
		temp_1 = self.searchUser(username)
		temp_2 = self.confirmPass(username, password)
		#print temp_1, temp_2, password
		if temp_1 == temp_2 == True:
			return True
		else:
			return False
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
		f = open("userlist.txt")
		users = {}
		for line in f:
			if not(line[0] == "\t"):
				temp = line.split(":")
				users[temp[0]] = temp[1].rstrip()
		f.close
		#print users
		return users