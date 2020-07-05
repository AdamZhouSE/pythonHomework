t=int(input())
for i in range(t):
    x=input()
    count=[]
    print(x)
    res=0
    temp=[]
    count=[]
    for i in range(1,len(x)-1):
        for j in range(len(x)-i):
            zero=0
            one=0
            two=0
            
            tmp=x[j:j+i+1]
            if tmp in temp:
                continue
            else:
                temp.append(tmp)
                for k in tmp:
                    if k=='0':
                        zero+=1
                    elif k=='1':
                        one+=1
                    else:
                        two+=1
                count.append(str(zero)+str(one)+str(two))
                
    count.sort()
    print(count)
    print(temp)