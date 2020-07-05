num=int(input())
name=[]
for i in range(0,num):
    name.append(input())
m=int(input())
called=[]
for i in range(0,m):
    call=input()
    if call in name:
        if call in called:
            print("REPEAT")
        else:
            print("OK")
            called.append(call)
    else:
        print("WRONG")