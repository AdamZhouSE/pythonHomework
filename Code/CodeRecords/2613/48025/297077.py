t=int(input())
def print_cornel(n):
    epoch_num_max=1
    epoch_num_counter=0
    last_num=0
    for i in range(0,n):
        if(last_num==0):
            print(1,end='')
            last_num+=1
            continue
        if(epoch_num_counter==epoch_num_max-1):
            last_num+=1
            print(end=' ')
            print(last_num,end='')
            epoch_num_max+=1
            epoch_num_counter=0
        else:
            last_num+=2
            print(end=' ')
            print(last_num,end='')
            epoch_num_counter+=1
    print()
for i in range(0,t):
    n=int(input())
    print_cornel(n)