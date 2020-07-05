n=int(input())
#print('n=',n)
N=list(input())
nn=len(N)
new=[]
for i in range(nn):
    if N[i].isdecimal():
        new.append(int(N[i]))
#print('new=',new)
for i in range(n-1):
    result='YES'
    if N[i+1]>N[i]:
        pass
    elif N[i+1]<N[i]:                  #升-降
        for j in range(i+1,n-1):
            if N[j+1]>=N[j]:           #升-降-升/平
                result='NO'
                break
            else:                      #升-降-降
                result='YES'
                break
    elif N[i+1]==N[i]:
        for j in range(i+1,n-1):
            if N[j+1]>N[j]:
                result='NO'  
                break                  #升-平-升
            elif N[j+1]<N[j]:
                for k in range(j+1,n-1):
                    if N[k+1]>=N[k]:
                        result='NO'
                        break          #升-平-降-升/平
                    else:
                        result='YES'
                        break          #升-平-降-降
print(result)