class Calculator:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
       
    def add(self):
        return self.a+self.b
        
    def difference(self):
        return self.a-self.b

    def multiply(self):
        return self.a*self.b
    
    def devide(self):
        return self.a/self.b

class sciencecalculator(Calculator):
    def power(self):
        return pow(self.a,self.b)

    
licz=Calculator(2,3)
liczlepiej=sciencecalculator(7,2)
print(liczlepiej.add())
print(liczlepiej.power())
print(licz.add())
print(licz.difference())
print(licz.multiply())
print(licz.devide())