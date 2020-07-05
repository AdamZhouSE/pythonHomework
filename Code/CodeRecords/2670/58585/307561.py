def find(x):
    if x<2 or x==2:
        return 2
    temp=2
    while(x>temp):
        temp*=2
    return temp

num=int(input())
for i in range(num):
    N=int(input())
    print(find(N)-N-1)