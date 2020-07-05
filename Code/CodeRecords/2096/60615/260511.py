num=int(input())

def squ(n):
    if n%2==0:
        count=n//2
    else:
        count=(n+1)//2
    while count*count>n:
        count=count-1
    return count
print(squ(num))