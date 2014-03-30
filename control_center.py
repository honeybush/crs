import factory

class CC:
	def __init__(self):
		self.factory = factory.Factory()
	def createUser(self, userInfo):
		self.newUser = self.factory.createUser(userInfo)
		self.inputUser(self.newUser)
	def inputUser(self, user):
		f = open("userlist.txt", "a")
		temp = user.username+":"+user.password+"\n"
		f.write(temp)
		temp = "\t"+user.ln+", "+user.fn+" "+user.mi+"\n"
		f.write(temp)
		temp = "\t"+user.type+"\n"
		f.write(temp)
		f.close()