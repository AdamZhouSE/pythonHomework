x=int(input())
y=int(input())
bound=int(input())
res =[]
I = 0
J = 0
while True:
    if pow(x,I)>=bound and pow(y,J)>=bound:
        break
    I+=1;
    J+=1;

for i in range(I):
    for j in range(J):
        temp = int(pow(x,i)+pow(x,j))
        if(temp<=bound):
            res.append(temp)
        else:
            break;

res.sort();
res = list(set(res))
if
print(res)