a,b,c = map(int, input("Please enter three integers: ").split())

if a>b == True and a>c ==True:
    print('{a} is greater'.format(a=a))
elif b>a == True and b>c == True:
    print('{b} is grater'.format(b=b))
else:
    print('{c} is greater'.format(c=c))
    