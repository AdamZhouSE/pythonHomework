n=int(input())
num_list=list(map(int,input().split()))
sum=num_list[0]
energy=0
for i in range(n-1):
    if num_list[i]-num_list[i+1]<0:
        if (energy+num_list[i]-num_list[i+1])>=0:
            energy+=num_list[i]-num_list[i+1]
        else:
            sum+=-(energy+num_list[i]-num_list[i+1])
            energy=0
    else:
        energy+=num_list[i]-num_list[i+1]
print(f'{sum}')
    
    
    