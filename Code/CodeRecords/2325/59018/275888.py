info=input().split(',')
a=[int(y) for y in info]
b=set(a)
for i in range(2,len(a)):
    if len(a)==i*len(b):
        print('True')
        break
else:
    print('False')
