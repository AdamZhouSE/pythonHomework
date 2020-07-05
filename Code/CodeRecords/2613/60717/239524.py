n=int(input())

for i in range(0,n):
    a=int(input())
    count1=1
    count2=0
    tmp=1
    strr=''
    for j in range(0,a):
        strr+=str(tmp)
        strr+=' '
        count2+=1
        if count2==count1:
            count2=0
            count1+=1
            tmp+=1
        else:
            tmp+=2
    print(strr)        


        
    