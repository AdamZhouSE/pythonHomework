temp=[int(x) for x in input().split(',')]
rs=0
for i in range(len(temp)-1):
    j=i
    k=i+1
    dis=temp[k]-temp[j]
    count=1
    while(k<len(temp)-1):
        j+=1
        k+=1
        if(temp[k]-temp[j]==dis):
            count+=1
            if(count>=2):
                rs+=1
        else:
            break
print(rs)