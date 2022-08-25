
l1 = [3, 6, 9, 12, 15, 18, 21,200]
l2 = [4, 8, 12, 16, 20, 24, 28,24,25,26]
# fininding even index number from l1
# 1
list1 = l1[0::2]
print(list1)
# 2
even = 0
iteration = len(l1) % 2
if iteration == 0:
    excute= int(len(l1) / 2)
else:
    excute = int((len(l1) +1) / 2)
evenList = []
for i in range(excute):
    evenList.append(l1[even])
    even+=2
print(evenList)

#finding odd index number from l2
# 1
list2 = l2[1::2]
print(list2)
# 2
odd =1
iteration2 =  len(l2) % 2
if iteration2 == 0:
    execute2 = int(len(l2) / 2)
else:
    execute2 = int((len(l2) -1) / 2)
oddList=[]
for j in range(execute2):
    oddList.append(l2[odd])
    odd+=2
print(oddList)