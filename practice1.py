#just revision of all basics

"""name = input("Enter your name")
age = int(input("Enter your age"))
branch = input("Enter your branch")
cgpa = float(input("Enter your cgpa"))


print("\n------Student Details------")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Branch: {branch}")
print(f"CGPA: {cgpa}")"""


#operators

"""a = float(input("Enter 1st num:  "))
b = float(input("ENter 2nd num:  "))

print("Addition: ",(a+ b))
print(f"Subtraction:{a-b} ")
print(f"Multiplication : {a*b}")
print(f"Divisio: {a/b}n")
print(f"Modulus: {a%b}")
print(f"Power : {a**b}")


print("a>b : ", a>b)
print("a === b: ", a==b)"""

#if-else 

"""marks = int(input("Enter marks: "))

if(marks  >= 90):
    print("Grade A")
elif marks >= 75 : 
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade Pass")
else: 
    print("Fail")"""

#loops

'''    num  = int(input("Enter a number: "))

    print(f"Multilpication table of {num}")

    for i  in range(1,11):
        print(f"{num} * {i} = {num * i}")'''

#while 

'''count  = 1
while count <=5 : 
    print(count)
    count +=1'''
#for with continue and break
"""for i in range(1,11):
    if(i == 5):
        continue
    if(i == 9):
        break
    print(i)A
"""

#Strings

'''text = input("Enter a sentence: ")

print(f"Uppercase: {text.upper()}")
print(f"Lower case: {text.lower()}")
print(f"Length: {len(text)}")
print("Reverse :", text[::-1])

print(f"Words : {len(text.split())}")'''

#palindrome

'''text = input("Enter a word: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")'''

#lists

'''marks = [34,22,33,45,21]

print("Marks: ", marks)
print("Highest: ", max(marks))
print("Lowest: ", min(marks))
print("Average: ", sum(marks)/len(marks))

marks.append(20)
marks.sort()

print("Updated: ", marks)'''

#tuples

'''student = ("ABC", 20, "cs")

print(student)
print(student[0],"\n", student[1],"\n",student[2],"\n")

name, age, branch = student
print(name)
print(age)
print(branch)'''

#sets

'''club_a = {"A","B","C","D","E"}
club_b = {"B","C","D","E","F"}
print(club_a)
print("Union : ", club_a.union(club_b))
print("Intersection : ", club_a.intersection(club_b))
print("Difference : ", club_a - club_b)


numbers = [1,2,2,2,3,4,4,5,6,6,7]

unique = set(numbers)

print(unique)'''

#dictionaries

'''student = {
    "name": "Abc",
    "age":20,
    "branch": "a",
    "cgpa":6.88
}

print(student["name"])
print(student["age"])

student["cgpa"] = 9.0

print(student["cgpa"])

print(student)

for key,value in student.items():
    print(key, ":", value)'''

#functions

def greet(name):
    print(f"Hellow, {name}")

greet("XYZ PERSON")

def add(a,b):
    return a+b
result = add(10,20)
print(result)

def welcome(name="XYZ"):
    print(f"Namskara {name}")

welcome()
welcome("abcd")