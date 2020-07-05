info=input().split(',')
a=[int(y) for y in info]
b=set(a)
for i in range(len(a)):
    if len(a)==i*len(b):
        print('True')
else:
    print('False')
