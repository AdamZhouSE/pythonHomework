def find_lcsubstr(s1, s2):
    m=[[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)]  
    mmax=0  
    p=0  
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                m[i+1][j+1]=m[i][j]+1
                if m[i+1][j+1]>mmax:
                    mmax=m[i+1][j+1]
                    p=i+1
    return s1[p-mmax:p],mmax   
n=int(input())
l1=input()
res=l1
for i in range(1,n):
    l2=input()
    res=find_lcsubstr(l1,l2)
    l1=res[0]
print(res[1])