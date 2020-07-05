n=int(input())
name=[]
for i in range(n):
    name.append(input())
called=[]
m=int(input())
for i in range(m):
    call=input()
    if name.count(call)==0:
        print('WRONG')
    elif called.count(call)!=0:
            print('REPEAT')
    else:
        print('OK')
        called.append(call)