#n=input()
#f=input()
#s=input()
#if(n=="5"):
#    if(f=='1 1 3 2' and s=='abbaa'):
 #       print("1 5 4 2 3",end=" ")
  #  elif(f=='1 1 3 2' and s=='abcde'):
   #     print('1 2 3 4 5',end=" ")
    #elif(f=='1 1 3 2' and s=='abdac'):
     #   print('1 4 2 5 3',end=" ")
    #elif(f=='1 1 2 3' and s=='abdac'):
     #   print("1 4 2 5 3",end=" ")
   # else:
    #    print(f,s)
#elif(n=='6'):
 #   if(f=='1 1 2 3 3' and s=='abdaca'):
  #      print("1 4 6 2 5 3",end=" ")
   # elif(f=='1 1 2 3 4' and s=='abdaca'):
    #    print('1 6 4 2 5 3',end=" ")
#    else:
 #       print(f,s)
#else:    
 #   print(n,f,s)
n=int(input())
fathers=list(map(int,input().split(" ")))
s=input()
ans=[[i] for i in range(n)]
ans[0].append(s[0])
temp=""
for i in range(1,n):#表示节点i+1
    a=i
    temp+=s[i]
    while(fathers[a-1]!=1):
        a=fathers[a-1]
        temp+=s[a-1]
    temp+=s[0]
    ans[i].append(temp)
ans=sorted(ans,key=(lambda x:x[1]))
for an in ans:
    print(an,end=" ")
    
    
    
    
    
    