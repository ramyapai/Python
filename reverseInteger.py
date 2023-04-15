number = int(input())
num = number
reverse = 0
for _ in range(len(str(number))):
    m = number % 10
    reverse = (reverse * 10) + m
    number = int(number /10)
print(reverse)    

if num == reverse:
    print("number is a palindrome")
else:
    print("number is not a palindrome")
    