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
        temp = int(pow(x,i)+pow(y,j))
        if(temp<=bound):
            res.append(temp)
        else:
            break;

res.sort();
res = list(set(res))
if(res==[2, 3, 4, 5, 6, 8, 9, 10, 12, 16]):
    print(x)
    print(y)
    print(bound)
print(res)