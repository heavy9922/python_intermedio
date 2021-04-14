from functools import reduce
my_list = [1,2,3,4,5,6,13,19,21]

obb = list(filter(lambda x : x % 2 != 0, my_list))

#print(obb)

listS = [1,2,3,4,5]
my_square = [i**2 for i in listS]

obb2 = list(map(lambda x : x**2, listS))

#print(obb2)

li = [2,2,2,2,2]

obb3=reduce(lambda a , b: a * b ,li)

print(obb3)