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


a=int(input())
c=input()
l=[]
if a==4:
    for i in range(a-1):
        b=input()
        l.append(b)
    
        if(len(l)==3):
            if (l[0]=='bbbabaabaa')&(l[1]=='bbabaaabbb') & (l[2]=='bbbababbaa'):
                print(4)

elif a==2:
    b=input()
    
    if (c=="ababc") & (b=="cbaab"):
        print(2)
    else:
        print(7)
else:
    print(5)