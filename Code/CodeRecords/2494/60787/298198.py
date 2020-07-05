num=eval(input())
re=0
for i in range(0,len(num)-1):
    for j in range(i+1,len(num)):
        if num[i]>2*num[j]:
            re+=1
print(re)