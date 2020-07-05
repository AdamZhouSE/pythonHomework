num=int(input())
t=[]
for i in range(num):
    t.append(list(input()))
flag=0

for i in range(0,num):
    for j in range(1,num):
        cou = 0
        if t[i-1][j]=="o" and i-1>=0: #and i-1<=num and j>0 and j<=num:
            cou+=1
        if i + 1 < num  and t[i +1][j] == "o":
            cou+=1
        if t[i][j - 1] == 'o' and j - 1 >= 0:
            cou+=1
        if j + 1 < num and t[i][j + 1]== 'o':
            cou+=1
        if cou%2==1:
            flag=1
            break
    if flag==1:
        break
if flag==1:
    print("NO")
else:
    print("YES")
