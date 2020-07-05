tests=(int)(input())
def splits(sum,i):
    if((int)(sum[i]/4)+(int)(sum[i]/3)+(int)(sum[i]/2)<=sum[i]):
        return sum
    else:
        return sum[:i]+[(int)(sum[i]/4),(int)(sum[i]/3),(int)(sum[i]/2)]+sum[i+1:]
for i in range(tests):
    n=(int)(input())
    sum=[n]
    temp=sum
    while(True):
        k=0
        length=len(sum)
        while(k<len(temp)):
            temp=splits(temp,k)
            if(temp!=sum):
                sum=temp
                k+=2
            k+=1
        if(len(sum)==length):
            break
    result=0
    for j in sum:
        result+=j
    print(result)