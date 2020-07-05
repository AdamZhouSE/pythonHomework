T=int(input())
for i in range(0,T):
    num=int(input())
    arr=[int(n) for n in input().split(' ')]
    new,re=[],[]
    for j in range(1,num+1):
        k=0
        new=[]
        while k<num:
           a=arr[k]
           if k+j<num:
              for n in range(k+1,k+j):
                 if arr[n]<a:
                     a=arr[n]
              new.append(a)
              k=k+1
           else:
              for n in range(num-j,num):
                  if arr[n]<a:
                      a=arr[n]
              new.append(a)
              k=k+1
        max=-1
        for m in range(0,len(new)):
           if new[m]>max:
               max=new[m]
        re.append(max)

    for j in range(0,num-1):
        print(re[j],end=" ")
    print(re[num-1])