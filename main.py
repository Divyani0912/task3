#import statistics
class firstclass:
    val1 = 0
    val2 = 0
    val3 = 0
    val4 = 0
    val5 = 0

    def __init__(self,a,b,c,d,e):
        print('This is constructor')
        self.val1 = a
        self.val2 = b
        self.val3 = c
        self.val4 = d
        self.val5 = e
        
    def addvalue(self):
        print(f'Addition = {self.val1 + self.val2 + self.val3 + self.val4 + self.val5}')

    def subValue(self):
        print(f'Substraction = {self.val1 - self.val2 - self.val3 - self.val4 - self.val5}')

    def mulValue(self):
        print(f'Multiplication = {self.val1 * self.val2 * self.val3 * self.val4 * self.val5}')

    def  divValue(self):
        print(f'Division = {self.val1 / self.val2 / self.val3 / self.val4 / self.val5}')

    def modValue(self):
        print(f'Modulus = {self.val1 % self.val2  % self.val3 % self.val4 % self.val5}')

    def meanValue(self):
        print(f'Mean = {(self.val1 + self.val2 +self.val3 + self.val4 + self.val5)/5}')

    def medianValue(self):
        Values = [self.val1, self.val2,self.val3,self.val4,self.val5]
        values.sort()
        median_value = Values[2]
        print(f'Median = {median_value}')

    def maxValue(self):
        values = [self.val1,self.val2,self.val3,self.val4,self.val5]
        print(f'Max = {max(values)}')

    def minValue(self):
        values = [self.val1,self.val2,self.val3,self.val4,self.val5]
        print(f'Min = {min(values)}')
    
    def per_75_50_25(self):
        print(f'75_percent_add = {(75*(self.val1 + self.val2 + self.val3 + self.val4 + self.val5))/100}')
        print(f'50_percent_add = {(50*(self.val1 + self.val2 + self.val3 + self.val4 + self.val5))/100}')
        print(f'25_percent_add = {(25*(self.val1 + self.val2 + self.val3 + self.val4 + self.val5))/100}\n')
        
        print(f'75_percent_sub = {(75*(self.val1 - self.val2 - self.val3 - self.val4 - self.val5))/100}')
        print(f'50_percent_sub = {(50*(self.val1 - self.val2 - self.val3 - self.val4 - self.val5))/100}')
        print(f'25_percent_sub = {(25*(self.val1 - self.val2 - self.val3 - self.val4 - self.val5))/100}\n')
        
        print(f'75_percent_mul = {(75*(self.val1 * self.val2 * self.val3 * self.val4 * self.val5))/100}')
        print(f'50_percent_mul = {(50*(self.val1 * self.val2 * self.val3 * self.val4 * self.val5))/100}')
        print(f'25_percent_mul = {(25*(self.val1 * self.val2 * self.val3 * self.val4 * self.val5))/100}\n')
        
        print(f'75_percent_div = {(75*(self.val1 / self.val2 / self.val3 / self.val4 / self.val5))/100}')
        print(f'50_percent_div = {(50*(self.val1 / self.val2 / self.val3 / self.val4 / self.val5))/100}')
        print(f'25_percent_div = {(25*(self.val1 / self.val2 / self.val3 / self.val4 / self.val5))/100}\n')
        
        print(f'75_percent_mod = {(75*(self.val1 % self.val2 % self.val3 % self.val4 % self.val5))/100}')
        print(f'50_percent_mod = {(50*(self.val1 % self.val2 % self.val3 % self.val4 % self.val5))/100}')
        print(f'25_percent_mod = {(25*(self.val1 % self.val2 % self.val3 % self.val4 % self.val5))/100}')
              
    f1 = firstclass(2,3,4,5,6)

    f1.addValue()
    f1.subValue()
    f1.mulValue()
    f1.divValue()
    f1.meanValue()
    f1.modeValue()
    f1.medianValue()
    f1.maxValue()
    f1.minValue()
    f1.per_75_50_25()

    print('f1.val1 = ',f1.val1)
    print('f1.val2 = ',f1.val2)
    print('f1.val3 = ',f1.val3)
    print('f1.val4 = ',f1.val4)
    print('f1.val5 = ',f1.val5)
