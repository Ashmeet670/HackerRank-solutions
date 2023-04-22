class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
        
    def computeDifference(self):
        
        
        for commonNum in self.__elements:
            for j in self.__elements:
                d = commonNum - j
                d = str(d)
                if d[0] == "-":
                   d = d.replace("-","")
                d = int(d)
                
                if d > self.maximumDifference:
                    self.maximumDifference = d
                     
                    


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)