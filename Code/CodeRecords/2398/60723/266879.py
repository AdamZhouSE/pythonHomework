def check(array,K,T_max):
    table=[0]*K
    for i in range(K):
        table[i]=array[i]
    table.sort()
    for i in range(K,len(array)):
        table[0]=table[0]+array[i]
        table.sort()
    return max(table)<=T_max
num=input().split()
N=int(num[0])
T_max=int(num[1])
array=[]
for i in range(N):
    array.append(int(input()))
for i in range(1,N+1):
    if check(array,i,T_max):
        print(i)
        break