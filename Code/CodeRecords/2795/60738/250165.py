n= int(input())
num_list=list(map(int,input().split(" ")))
num_list.sort()
num_1=num_list[0]
value=0
def func(num_list,n):
    time=0
    for i in range(n-1):
        if num_list[i]!=num_list[i+1]:
            time+=1
            if time==3:
                return -1
    for j in range(n):
        if num_list[j]!=num_1:
            value=num_list[j]-num_1
            if time==1 and value%2==0:
                value=int(value/2)
            for k in range(j,n):
                if num_list[k]!=num_list[j]:
                    if value!=num_list[k]-num_list[j]:
                        return -1
                    return int(value)
    return value
print(func(num_list,n))