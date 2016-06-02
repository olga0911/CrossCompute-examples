class Student(object):

	
	def first_name(self, name):
			self.first_name = name
			print name
		

	def last_name(self, name):
			self.last_name = name
			print name

	def greetings(self):
			print ("Welcome %s" % self.first_name)

student1 = Student()
student1.first_name("Olga")
student1.last_name("Lee")
student1.greetings()
