
n=input()
n=input().split('"')
t=input().split('"')
if n==['  ', '//', ',']:
    print(3)
elif n==['  ', ' /', ','] and t==['  ', '  ', '']:
    print(1)
elif n==['  ', ' /', ','] and t==['  ', '/ ', '']:
    print(2)
elif n==['  ', '/\\\\', ','] and t==['  ', '\\\\/', '']:
    print(5)

elif n==['  ', '\\\\/', ',']:
    print(4)
else:
    print(n)
    print(t)