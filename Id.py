a =10
print("the id for a is:", id(a) , "value of a is:", a)

list1 =[5, 4, 3, 2, 1]
list2 =list1
list1 += [1, 2, 3, 4]

print(list1)
print(list2)

list1 =[5, 4, 3, 2, 1]
list2 = list1
list1 = list1 + [1, 2, 3, 4]

print(list1)
print(list2)

x = 5
y = 5
print(x is y)

w = ["Ramya", "Pai"]
z = ["Ramya", "Pai"]
print(w is z)
print(id(w))
print(id(z))

