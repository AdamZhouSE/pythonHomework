A=eval(input())
X=[]
Y=[]
for i in A:
    m=int(i)
    if (m%2==0):
        X.append(m)
    else:
        Y.append(m)
X.extend(Y)
print(X)