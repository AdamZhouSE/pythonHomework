a = input()
b = input()

if len(a) < len(b):
    print(0)
else:
    for i in range(len(a)-len(b)+1):
        for