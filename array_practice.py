
sum = 0
#largest
'''largest = n[0]
for i in n:
    if i > largest:
        largest = i
print(largest)
#print(max(n))


#smallest 
smallest = n[0]

for j in n:
    if smallest > j:
        smallest = j

print(f"Smallest: {smallest}")'''
#sum and avg
'''for i in n:
    sum += i

print(sum)

for i in n:
    sum += i
avg = sum/len(n)
print(avg)'''

#even odd count 
'''even = 0
odd = 0
for i in n:
    if(i%2 ==0):
        even +=1
    else:
        odd +=1

print(f"Odd : {odd}, Even : {even}")'''

#reverse
'''n = [-10, -5, -20]
j = []
i = len(n)-1
while i>=0:
    j.append(n[i])
    i -=1
print(j)'''


#key found or not 
n = [-10, -5, -20]
j = -20
for i in n:
    if i == j:
        print("Key found")
        break
    else: i+=1
