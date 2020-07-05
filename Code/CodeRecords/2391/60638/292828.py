n=int(input())
names=[]
res=[]
for i in range(0,n):
    names.append(input())
k=int(input())
for i in range(0,k):
    name=input()
    if names.__contains__(name):
        if res.__contains__(name):
            print('REPEAT')
        else:
            print('OK')
            res.append(name)
    else:
        print("WRONG")