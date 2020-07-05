a=eval(input())
for i in range(a):
    b=input()
    k1=eval(input())
    max1=-1
    for i in range(len(b)):
        for j in range(i+1,len(b)+1):
            s=b[i:j]
            count={}
            temp=0
            for k in s:
                if k not in count:
                    count[k] = 1
                else:
                    count[k] += 1
            dif=len(count)
            if(dif==k1):
                for k in count:
                    temp+=count[k]
            if(temp>max1):max1=temp
    print(max1)
