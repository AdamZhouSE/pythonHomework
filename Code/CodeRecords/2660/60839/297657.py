n=int(input())
op=[]
s=""
ans=[]
for i in range(0,n):
    op.append(input().split(" "))
for operation in op:
    if operation[0]=="T":
        s=s+operation[1]
    elif operation[0]=="U":
        for i in range(0,int(operation[1])):
            s=s[:len(s)-1]
    elif operation[0]=="Q":
        ans.append(s[int(operation[1])-1])
for i in ans:
    print(i)