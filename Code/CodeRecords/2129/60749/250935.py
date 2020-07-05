n=int(input())
def count_num(n):
    count=0
    while not n==1:
        if n%2==0:
            n=n/2
            count+=1
        else:
            n=n-1
            count+=1
    return count
print(count_num(n))