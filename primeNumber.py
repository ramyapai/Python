number = int(input("Please input the number to check if it is prime: "))
i, temp =0, 0
for i in range(2, number//2):
    if number%i ==0:
        temp == 1
        break
    
if temp == 1 :
        print('{number} is not prime'.format(number = number))
else:
        print('{number} is prime'.format(number=number))

    
