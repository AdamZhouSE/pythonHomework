rb=input()
b=list(map(int,input().split()))
a=[]
for i in range(len(b)-1):
    a.append(b[i]+b[i+1])
a.append(b[len(b)-1])
print(" ".join(list(map(str,a))))