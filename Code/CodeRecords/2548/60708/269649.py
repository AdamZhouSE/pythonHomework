N=int(input())
for n in range(0,N):
    str=input()
    k=int(input())
    maxlength=0
    for i in range(k,len(str)+1):
        for j in range(0,len(str)+1-k):
            temp=str[j:j+i]
            templist=set(list(temp))
            if len(templist)==k:
                if(len(temp)>maxlength):
                    maxlength=len(temp)
    print(maxlength)

