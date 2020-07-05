numOfEg=int(input())
num_list=[]
def max_side(num,n):
    if n==1:
        return 1
    for i in range(n):
        if num[i]<i+1:
            return i
    return n
            
    
for i in range(numOfEg):
    n=int(input())
    num_list=list(map(int,input().split(" ")))
    num_list.sort()
    num_list.reverse()
    print(max_side(num_list,n))
    