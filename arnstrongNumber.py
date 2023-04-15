number = int(input("Please give a number: "))
num = number
armstrong = 0
for _ in range(len(str(number))):
    m = number % 10
    armstrong = armstrong + pow(m,3)
    number = int(number /10)
    
print('the armstrong number is : {armstrong}'.format(armstrong=armstrong))

if num == armstrong:
    print("Number is armstrong")
else:
    print("number is not armstrong")