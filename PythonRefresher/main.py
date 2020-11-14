import keyword
import math as trigGod
import mymodule
import mymodule1

print("hello world")

my_var = 10
print(my_var)
print(type(my_var))
print(id(my_var))

print(keyword.kwlist)

s = ''' it's good to learn "programing" '''
print(s)

noneVar = print("print function does not return anything to the var")
print(type(noneVar))

#taking input from the user
#x = input("enter number: ") #takes input as string
#print(int(x)+1)

x = range(5)
print(x)
print(type(x))
#range object is immutabe

#while loop syntax
i = 0
while i < 6:
    print(i)
    i += 1

#for loop syntax
for x in range(3):
    print(x, "stinky")

#break and continue
l = [ 10, 54, 2, 61, 15]
n = int(input("enter search key: "))

for i in l:
    print(i,n)
    if i == n:
        print("found")
        break

for i in l:
    if i%2==0:
        continue
    print("ODDDD")

#lists
L = [10, "hello", 5.25]
print(L[0])
L1 = L + [33, "people"]
print(L1)
L.insert(1,20)
print(L)
L.append("poo poo")
print(L)
L.extend([33,777])
print(L)
print(L[0:3])

L2 = L[:] #the empty slice can be used to copy lists without them being connected
L[0] = "new"
print(L)
print(L2)

s = "a lengthy sentence"
L = s.split()
print(L)
print(type(L))
print(len(L))

#membership and identity operators

l1 = [10,54,2,61,15]
l2 = [10,54,2,61,15]
print(10 in l1)
print(l1 is l2)

#dictionaries
D = {'USA':100, 2:200, "uk":300}
print(D[2])
print(D.keys())
print('uk' in D)

#functions
def my_add(a,b):
    c = a + b
    return c

print(my_add(1,2))

def variable_parameters(*a):
    print(type(a))
    for i in a:
        print(i)

variable_parameters(1,2,"erd","blua")

#importing modules
print(dir(trigGod))
print(trigGod.pi)

mymodule.Display()
mymodule1.Display()

#class in python
class Student:
    '''this is version 1.0 student'''  #this documentation string is optional
    def __init__(self,name,grade): #constructor
        self.name = name
        self.grade = grade #these are instance variables

    def __str__(self):
        return "This is a student class"

    def display(self):
        print("Student name:", self.name)
        print("Grade:", self.grade)

S = Student("Abe","S")
print(S.name)
print(S.grade)
print(S.__doc__)
print(S.__str__())
S.display()

S1 = Student("NAbs", "A*")
S1.display()

S = [Student("Penis","f"), Student("bobby the kid", "only tony knows")]

for i in S:
    i.display()

