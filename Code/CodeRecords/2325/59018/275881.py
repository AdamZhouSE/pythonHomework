print(input())
b=set(a)
for i in range(len(a)):
    if len(b)==i*len(a):
        print('True')
else:
    print('False')
