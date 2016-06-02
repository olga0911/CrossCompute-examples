import sys


class Student(object):

    def first_name(self, name):
        self.first_name = name
        print name
		
    def last_name(self, name):
        self.last_name = name
        print name

    def greetings(self):
        print ("Welcome %s" % self.first_name)


first_name, last_name = sys.argv[1:]


student1 = Student()
student1.first_name(first_name)
student1.last_name(last_name)
student1.greetings()
