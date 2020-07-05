n= int(input())
def count_func(length):
    if(length==1):
        return 2
    elif(length==2):
        return 3
    else :
        return count_func(length-1)+count_func(length-2)
for i in range(n):
    a=int(input())
    print(f'{count_func(a)%1000000007}')
