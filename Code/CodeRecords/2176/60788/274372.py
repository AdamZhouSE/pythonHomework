def exchange(para,i,j):
    temp=para[j]
    para[j]=para[i]
    para[i]=temp
    return


str=list(input(""))
index=[x for x in range(len(str),0,-1)]
for i in range(0,len(str)-1):
    for j in range(0,len(str)-i-1):
        if str[j]>str[j+1]:
            exchange(str,j,j+1)
            exchange(index,j,j+1)
for k in range(0,len(index)):
    print(index[k],end="")
    if k!=len(index)-1:
        print(' ',end="")
print()
        
            