tests=(int)(input())
for i in range(tests):
    length=(int)(input())
    arr=input().split(' ')
    judge='No'
    for j in range(length):
        for k in range(j+1,length):
            sumj=0
            sumk=0
            for m in range(0,j+1):
                sumj+=(int)(arr[m])
            for n in range(0,k+1):
                sumk+=(int)(arr[n])
            if(sumj==sumk):
                judge='Yes'
        if(judge=='Yes'):
            break
    print(judge)