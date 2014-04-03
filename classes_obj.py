class Course:
	def __init__(self, courseInfo):
		self.courseInfo = courseInfo
		self.course = ""
		self.section = ""
		self.daySlot = []
		self.timeSlot = ""
		self.prof = ""
		self.students = []
		self.setDetails()
		self.setSection()
	def setDetails(self):
		self.course = self.courseInfo.get("course")
		self.timeSlot = self.courseInfo.get("time slot")
		self.daySlot = self.courseInfo.get("day slot")
		self.prof = self.courseInfo.get("prof")
	#def setDaySlot(self):
	#	temp = self.courseInfo.get("day slot")
	#	s = ""
	#	for i in temp:
	#		s = s+i
	#	return s
	def setSection(self):
		timeSlots = ("7:00-8:30", "8:30-10:00", "10:00-11:30", "11:30-1:00", "1:00-2:30", "2:30-4:00", "4:00-5:30", "5:30-7:00")
		letters = ("A", "B", "C", "D", "E", "F", "G", "H")
		temp = ""
		temp2 = ""
		temp3 = ""
		for t, l in zip(timeSlots, letters):
			if self.timeSlot == t:
				temp = l
		for d in self.daySlot:
			temp2 = temp2+d[0]
		subject = self.course.split()
		if len(subject) > 1:
			for s in subject:
				temp3 = temp3+s[0]
		else:
			temp3 = s[0:4]
		self.section = temp3.lower()+temp2.lower()+temp