number = int(input("Please enter the given number: "))
sum = 0

for _ in range (len(str(number))):
    sum = sum + number % 10
    number = number//10
    
print("Sum of digits is {sum}".format(sum=sum))    