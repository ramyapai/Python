a, b = map(int, input("please enter two numbers: ").split())

a = a+b
b = a-b
a = a-b

print("{a} is swapped value of a".format(a=a))
print("{b} is swapped value of b".format(b=b))