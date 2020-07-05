couples=list(map(int,eval(input())))
count=0
for i in range(0,len(couples),2):
    cp=couples[i]^1
    if(couples[i+1]!=cp):
        for j in range(i+1,len(couples)):
            if(couples[j]==cp):
                count+=1
                temp=couples[i+1]
                couples[i+1]=couples[j]
                couples[j]=temp
print(count)