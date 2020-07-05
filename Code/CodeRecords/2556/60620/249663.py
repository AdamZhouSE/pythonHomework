N,K=map(int,input().split())
X=[]
Y=[]
for i in range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)
result=[]
num=0
for i in range(N):
    for j in range(i+1,N):
        if(abs(X[i]-X[j])<K and abs(Y[i]-Y[j])<K):
            num+=1
            result.append(X[i])
            result.append(X[j])
            result.append(Y[i])
            result.append(Y[j])
if(num==0):print(0)
elif(num>=2):print(-1)
else:
    answer=(K-abs(result[0]-result[1]))*(K-abs(result[2]-result[3]))
    print(answer)