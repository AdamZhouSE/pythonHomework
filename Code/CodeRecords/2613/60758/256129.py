num=int(input())
for lll in range(0,num):
    num_list=[]
    num_list.append(1)
    n=int(input())
    i=2
    while (i-1)*(i)/2<n:
        current_num=num_list[-1]+1
        for j in range(0,i):
            num_list.append(current_num)
            current_num+=2
        i+=1
    for k in range(0,n):
        if(k!=n-1):
            print(num_list[k],end=" ")
        else:
            print(num_list[k])