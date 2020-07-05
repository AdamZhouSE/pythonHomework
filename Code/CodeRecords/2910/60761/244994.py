n=int(input())
hsequence=[]
result="YES"
for i in range(n):
    wi,hi=map(int,input().split(" "))
    if(i==0):
        hsequence.append(max(wi,hi))
    else:
        if(hi>hsequence[i-1]):
            if(wi>hsequence[i-1]):
                result="NO"
                break
            else:
                hsequence.append(wi)
        elif(wi<=hsequence[i-1]):
            hsequence.append(max(wi,hi))
        else:
            hsequence.append(hi)
print(result)
