class ClassName:
	"""docstring for ClassName"""
	def createName(self,name):
		self.name=name
	def displayName(self):
		return self.name
	def saying(self):
		print "hello %s" % self.name

ClassName
first=ClassName()
second=ClassName()
first.createName('Olga')
second.createName('Tony')