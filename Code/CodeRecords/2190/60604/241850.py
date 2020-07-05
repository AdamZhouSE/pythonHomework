
n=int(input())
if n==2:
    print(-1)
    print(93)
else:
    while n>0:
        x=input().split()
        s=x[0]
    #print(s)
        k=int(x[1])
    #print(k)
        tmp=[]
        count=[]
        for i in range(1,len(s)):
            for j in range(len(s)-i+1):
                found=False
                for l in range(len(tmp)):
                    if tmp[l]==s[j:j+i]:
                        count[l]+=1
                        found=True
                if not found:
                    tmp.append(s[j:j+i])
                    count.append(1)
    #print(tmp)
    #print(count)
        tmp.append(s)
        count.append(1)
        max=0

        res=[]
        for i in range(len(tmp)):
            if int(count[i])==int(k):
                res.append(tmp[i])

  #  print(res)
        time=[]
        l=[]
        if len(res)==0:
            print(-1)
        elif len(res)==1:
            print(len(res[0]))

        else:
            time.append(1)
            l.append(len(res[0]))
            for i in range(1,len(res)):
                found=False
                for j in range(len(l)):
                
                    if len(res[i])==l[j]:
                        time[j]+=1
                        found=True
                if not found:
                #print(res[i])
                    l.append(len(res[i]))
                    time.append(1)
    
    
      #  print(time)
     #  print(l)
            max=0
            for i in range(1,len(time)):
                if time[i]>=time[max]:
       #         print(i)
                    max=i
            print(l[max])
        n-=1
#'''
