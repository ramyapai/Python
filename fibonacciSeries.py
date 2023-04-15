number = int(input())
a,b = 1,1
c, i =0,0
print(a)
print(b)
for i in range(number):
    if number<1:
        print(i)
    else:
        c = a + b
        a = b
        b = c
        print(c)
    