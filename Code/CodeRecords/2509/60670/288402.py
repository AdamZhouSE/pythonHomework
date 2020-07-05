n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
m=int(input())
for i in range(0,m):
    op=input()
    operation=''
    if len(op)>3:
        op=op.split(' ')
        operation=op[0]
    if operation=="add":
        l.append(int(op[1]))
    else:
        l=sorted(l)
        print(l[(len(l)+1)//2-1])