a=eval(input())
print('[',end='')

first=True

for i in a:
    if(i%2==0):
        if(not first):
            print(', ',end='')
        print(i,end='')
        first=False;

for i in a:
    if(i%2!=0):
        if(not first):
            print(', ',end='')
        print(i,end='')
        first=False

print(']')
