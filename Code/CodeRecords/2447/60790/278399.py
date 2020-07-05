s=input().split()
m=int(s[0])
n=int(s[1])
charge=input().split()
charge=list(map(int,charge))
result=[]
for i in range(0,n):
    t=input().split()
    begin=int(t[0])-1
    end=int(t[1])-1
    result.append(min(charge[begin:end+1]))
for j in result:
    print(j,"",end='')