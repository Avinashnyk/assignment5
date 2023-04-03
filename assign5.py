#All the challenges are in this file

'''Challenge 1:'''
class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sqSum(self):
        print('Square of each number: 'f"{self.x**2},{self.y**2},{self.z**2}")
        print('Sum of squares:',self.x**2+self.y**2+self.z**2)
        
x=int(input('Enter 1st number: '))
y=int(input('Enter 2nd number: '))
z=int(input('Enter 3rd number: '))
p1=Point(x,y,z)
p1.sqSum()

'''Challenge 2:'''

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def addition(self):
        print('Addition of  numbers: ',self.num1+self.num2)
    def subtraction(self):
        if self.num1 >self.num2:
            print('Subtraction of numbers: ',self.num1-self.num2)
        else:
            print('Subtraction of numbers: ',self.num2-self.num1)
    def multiplication(self):
        print('Multiplication of numbers: ',self.num1*self.num2)
    def division(self):
        if self.num1 != 0 and self.num2 >= self.num1:
            print('Division of numbers: ',self.num2/self.num1)
        elif self.num2 != 0 and self.num1 >= self.num2:
            print('Division of numbers:',self.num1/self.num2)
        elif self.num1 == 0 or self.num2 == 0:
            print('Enter a number other than Zero for Division.')
num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
calc= Calculator(num1,num2)

calc.addition()
calc.subtraction()
calc.multiplication()
calc.division()


'''challenge 3:'''
class Student:
    def setname(self,name):
        self.__name= name
    def getname(self):
        return self.__name
    def setrollnumber(self,rollnumber):
        self.__rollnumber= rollnumber
    def getrollnumber(self):        
        return self.__rollnumber

name = input('Enter a name: ')
rollnumber= int(input('Enter rollnumber: '))
s= Student()
s.setname(name)
s.setrollnumber(rollnumber)
s.getname()
s.getrollnumber()
print("Name of the Student is",s.getname(),"with RollNumber ",s.getrollnumber())


'''challenge 4'''
class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance


class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestrate=0):
        super().__init__(title,balance)
        self.interestrate=interestrate
x=input('Enter a name: ')
y=int(input('Enter the balance: '))
z=float(input('Enter an interestrate: '))
s1=SavingsAccount('John',5000,2.5)
print('Account Holder ',s1.title,'has balance of ',s1.balance,'with an interestrate of ',s1.interestrate)

'''challenge 5'''
class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance

    def withdrawal(self,amount):
        if self.balance >= amount:
            self.balance = self.balance-amount
        else:
            print('Insufficient Balance')
    def deposit(self,amount):
        self.balance=self.balance + amount

    def getbalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestrate=0):
        super().__init__(title,balance)
        self.interestrate=interestrate
    def interestAmount(self):
        interestamount= (self.interestrate * self.balance)/100
        return interestamount
    
a= input('Enter a name: ')
b=float(input('Enter Balance: ',))
c=float(input('Enter interestrate: '))
d= float(input('Enter the amount to be deposited: '))
e=int(input('Enter the amount to be withdrawn: '))
s1=SavingsAccount(a,b,c)
s1.deposit(d)
print(s1.getbalance())

s1.withdrawal(e)
print(s1.getbalance())
print(s1.interestAmount())