#  two sum problem
# given number [1,2,6,3,7,8] target value is 9.

# 1. gettting all those two numbers which sum will return 9
numbers = [1,2,6,3,7,7]
prevousValue = None

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i]+ numbers[j] == 9:
            print(numbers[i], numbers[j])

#  2. getting the first match for the problem
num2= None
num3 = None
for i in range(len(numbers)):
    if num2 and num3 != None:
        if num2 + num3 == 9:
            break
    for j in range(len(numbers)):
        if numbers[i]+ numbers[j] == 9:
            print(numbers[i], numbers[j])
            num2 = numbers[i]
            num3 = numbers[j]
            break

