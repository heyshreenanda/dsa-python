#reverse string without using slicing

'''str = "Hello"
reverse = ""

i = len(str) - 1

while i >=0:
    reverse += str[i]
    i -= 1

print(reverse)'''


#count vowels

'''str = "Shreenanda"
str = str.upper()
vowels = "AEIOU"
count = 0
for ch in str:
    if ch in vowels:
        count += 1
print(f"Total number of vowels are : {count}")'''


#count uppercase, lower case, numbers and special characters 

text = "Hellow123@2025"
num_count = 0
char_count = 0
lower_count = 0
upper_count = 0

for ch in text:
    ascii_value = ord(ch)
    if ascii_value >= 65 and ascii_value <= 90:
        upper_count += 1
    elif ascii_value >= 97 and ascii_value <= 122:
        lower_count += 1
    elif ascii_value >= 48 and ascii_value <= 57:
        num_count += 1
    else: char_count += 1

print(f"Total counts are \n Upper case: {upper_count} \n Lower case: {lower_count} \n Digits :{num_count}\n Special characters: {char_count}")