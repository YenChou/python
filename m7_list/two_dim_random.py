import random
'''
list1 = [45,12,13,15,45,8]
list2 = []
for i in range(6):
    list2.append(random.randint(1,100))
print(list2)
for i in range(len(list1)):
    print(i,list1[i])
for s in list1:
    print(s)
else:
    print('nothing')
'''
row = eval(input('Row number: '))
col = eval(input('Col number: '))
list1 = []
for i in range(row):
    list1.append([])
    for j in range(col):
        list1[i].append(random.randint(1,100))
print(list1)