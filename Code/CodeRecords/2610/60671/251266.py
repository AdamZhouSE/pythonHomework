time=int(input())
while(time>0):
    time-=1
    length=int(input())
    str1=input()
    list1=str1.split()
    strnum=""
    for x in list1:
        strnum+=x
    #strnum="".join(numlist)
    for x in range(len(strnum)):
        for i in range(len(strnum) - x):
            list1.append(strnum[i:i + x + 1])
    sameCount=0
    for s in list1:
        lenn=len(s)
        haveSame=False
        for i in range(lenn-1):
            for j in range(i+1,lenn):
                if(s[i]==s[j]):
                    haveSame=True
                    break
            if(haveSame):
                break
        if(haveSame):
            sameCount+=1
    num=length*(2**(length-1))-1
    print(num-sameCount)