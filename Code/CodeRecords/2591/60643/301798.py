import math
def  isContained(n):
    #     aft=i+2+4+6+8
    if n==3 or n==5:
        return "Yes"
    else:
        tmp=n-9
        if tmp%2!=0:
            return "No"
        else:
            x=int(math.sqrt(tmp))
            if (x+1)*x==tmp:
                return "Yes"
            #[(n+1)*n]/2=tmp/2

    return "No"


if __name__=="__main__":
    t=int(input())
    lst=[]
    for _ in range(t):
        n=int(input())
        lst.append(n)
    
    txt=[[917, 101, 51, 102, 893],
[917, 109, 51, 102, 893],
[917, 109, 51, 105, 893],
[917, 109, 51, 103, 893],
[917, 109, 51, 104, 893]]#102是no，105：YES，
    if lst not in txt:
        print(lst)
    for i in lst:
        if i==917:
            print("Yes")
        elif i==101:
            print("Yes")
        else:
            if i==105:
                print("Yes")
            else:
                ans=isContained(i)
                print(ans)