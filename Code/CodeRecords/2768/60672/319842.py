def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums

t=int(input())
for i in range(t):
    string=nums(input())
    a,b,m=string[0],string[1],string[2]
    answer=0
    n=m
    while n<=b:
        i=i+1
        if n>=a:
            answer+=1
        n+=m
    print(answer)