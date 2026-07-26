'''#*args

def total_marks(*marks):
    print("Marks: ", marks)
    print("Total : ", sum(marks))

total_marks(90,45,33,22)

# **kwargs

def student_details(**students):
    for key, value in students.items():
        print(f"{key}:{value}")

student_details(
    name="ABCD",
    age = 20,
    branch = "cse"
)

# lambda 

square = lambda x: x*x
print(square(3))

numbers = [5,3,6,2]

numbers.sort(key = lambda x:x)
print(numbers)'''

#file handling
'''with open("notes.txt","w") as file:
    file.write("Python practice\n")
    file.write("Learning new concepts")'''

'''with open("notes.txt", "r") as file:
    print(file.read())'''

'''with open("notes.txt","a") as file:
    file.write("\nPracticing the concepts")'''

#exception handling

'''try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    print(f"Division of{a},{b} is: {a/b}")

except ZeroDivisionError:
    print("Cannot divide by zero...")

except ValueError:
    print("Enter only numbers.")

finally:
    print("Program completed....")'''

#oop concepts

'''class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Details.....!!!!")
        print("Name: ", self.name)
        print("Age: ",self.age)

stu1 = Student("ABC",20)
stu1.display()'''

class BackAccount:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited successfully: ", amount)

    def withdraw(self, amount):
        if(amount<= self.balance):
            self.balance -= amount
            print("Withdraw successful: ", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Available Balance: ", self.balance)

acc1 = BackAccount("Shreenanda", 10000)

acc1.deposit(9000)
acc1.withdraw(25000)
acc1.show_balance()