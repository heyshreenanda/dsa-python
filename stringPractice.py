#reverse string without using slicing

'''str = "Hello"
reverse = ""

i = len(str) - 1

while i >=0:
    reverse += str[i]
    i -= 1

print(reverse)'''


#count vowels

str = "Shreenanda"
str = str.upper()
vowels = "AEIOU"
count = 0
for ch in str:
    if ch in vowels:
        count += 1
print(f"Total number of vowels are : {count}")

    