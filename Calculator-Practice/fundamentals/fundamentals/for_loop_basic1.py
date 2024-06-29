# functions in python

for i in range(0, 151):
    print(i)

for i in range(5, 1005, 5):
    print(i)

for i in range(1, 101):
    if i % 5 == 0:
        print("Coding")
    if i % 10 == 0:
        print("Dojo")

sum = 0
for i in range(0, 500001):
    if i % 2 != 0:
        sum = sum + i
print(sum)


for i in range(2018, 0, -4):
    print(i)

lowNum = 2
highNum = 9
mult = 3


while lowNum <= highNum:
    if lowNum % 3 == 0:
        print(lowNum)
    lowNum = lowNum + 1
