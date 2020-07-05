m=int(input())
n=int(input())
op=int(input())
ops=[]
M=[[0 for i in range(n)] for j in range(m) ]
for k in range(op):
    a,b=map(int,input().split(","))
    for i in range(min(a,m)):
        for j in range(min(b,n)):
            M[i][j]+=1
result=[]
for s in M:
    result+=s
print(result.count(max(result)))
    
