def cracksafe(n,k):
    sumnum=pow(k,n)
    sb=""
    for x in range(n):
        sb+="0"
    set1=[]
    set1.append(sb)
    for i in range(1, sumnum):
        tempstring=sb[len(sb)-n+1:]
        for j in range(k-1,-1,-1):
            temp=tempstring+str(j)
            if not temp in set1:
                sb+=str(j)
                set1.append(temp)
                break
    return sb
n=int(input())
k=int(input())
print(cracksafe(n,k))