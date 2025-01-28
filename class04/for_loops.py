"""
For loops
iterate over collection, each character
"""

for item in 'Python':
    print(item)
for number in [1,2]:
    print(number)
for names in ['Souji', 'Tej', 'Ratna']:
    print(names)
for a in range(5,10,2):
    print(a)
prices = [10,20,30]

total = 0
for price in prices:
    total += price
print("total", total)

for x in range(2):
    for y in range(1):
        print(x,y)
numbers = [5,2,5,2,2]
for x_counts in numbers:
    print('x' * x_counts)

count = [2,23,43,22,55]
max = count[0]
for z in count:
    if z>max:
        max = z
print(max)
#for loop
