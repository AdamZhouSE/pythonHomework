num=int(input())
test=[]
xx=[]
el=[]
for i in range(num):
    test.append(list(input()))

for i in range(num):
    for j in range(len(test[0])):
        if j==num-i-1 or j==i:
            xx.append(test[i][j])
        else:
            el.append(test[i][j])
a=set(xx)
b=set(el)
if len(a)==1 and len(b)==1 and a!=b:
    print("YES")
else:
    print("NO")