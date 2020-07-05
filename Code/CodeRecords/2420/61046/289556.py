test=int(input())
res=[0]*2
temp=list(str(test-1))
flag=0
count=0
for i in range(1,test):
    temp = list(str(test - i))
    for x in temp:
        if x == "0":
            flag = 1
            count+=1
            break
        else:
            flag=0
    if flag==0:
        count+=1
        break

res[0]=count
res[1]=test-count
print(res)
