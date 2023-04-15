num = int(input("Please enter the number: "))
temp =0
for _ in range(len(str(num))):
    if num%10 == 0:
       temp =1
    elif num%10 == 1:
        temp =1
    else: 
        temp =0 

if temp ==1:       
    print("{num} is  binary".format(num=num))
else:
    print("{num} is not binary".format(num=num))        