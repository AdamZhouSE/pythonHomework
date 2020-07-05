info=input().split(',')
a=[int(y) for y in info]
b=set(a)
for i in range(len(a)):
    if len(b)==i*len(a):
        print('True')
else:
    print('False')
