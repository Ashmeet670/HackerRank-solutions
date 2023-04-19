class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
                
                

class Student(Person):
    
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

        
    def calculate(self):
        
        totalScore = 0
        for i in self.scores:
            totalScore += i
        
        
        score = totalScore/len(self.scores)
        
        if score >= 90:
            return "O"
        elif score >= 80:
            return "E"
        elif score >= 70:
            return "A"
        elif score >= 55:
            return "P"
        elif score >= 40:
            return "D"
        elif score < 40:
            return "T"
            


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())