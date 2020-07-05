t=int(input())
for i in range(t):
    x=input()
    count=0
  #  print(x)
    res=0

    for i in range(1,len(x)-1):
        for j in range(len(x)-i):
            zero=0
            one=0
            two=0
            
            tmp=x[j:j+i+1]
            for k in tmp:
                if k=='0':
                    zero+=1
                elif k=='1':
                    one+=1
                else:
                    two+=1
            if zero==one and zero==two:
                count+=1
                
                

    print(count)
   # print(temp)




































