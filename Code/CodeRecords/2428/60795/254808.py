T=int(input())
for i in range(0,T):
    num=int(input())
    arr=[int(n) for n in input().split(' ')]
    odd=[]
    even=[]
    for j in range(0,num):
        if arr[j]%2==0:
            even.append(arr[j])
        else:
            odd.append(arr[j])
    for j in range(0,len(odd)):
        for k in range(j+1,len(odd)):
            if odd[j]<odd[k]:
                odd[j],odd[k]=odd[k],odd[j]
    for j in range(0,len(even)):
        for k in range(j+1,len(even)):
            if even[j]>even[k]:
                even[j],even[k]=even[k],even[j]
    re=[]
    for j in range(0,len(odd)):
        re.append(odd[j])
    for j in range(0,len(even)):
        re.append(even[j])
    for j in range(0,num):
        print(re[j],end=" ")
    print("")