tests=(int)(input())
def remainder(x):
    return (int)(x)%3
for i in range(tests):
    n=(int)(input())
    arr=map(remainder,input().split(' '))
    sum=0
    count0,count1,count2=0,0,0
    for i in arr:
        if(i==0):
            count0+=1
        elif(i==1):
            count1+=1
        else:
            count2+=1
    print(count0+min(count2,count1)+(int)(abs(count1-count2)/3))

