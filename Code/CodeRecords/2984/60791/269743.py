a = input()
b = input()

if(a == b):
    print(2)
elif(len(a) != len(b)):
    print(1)
elif(a.lower() == b.lower()):
    print(3)
else:
    print(4)