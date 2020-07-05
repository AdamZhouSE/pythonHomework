n=int(input())
for i in range(int(n/2)+1):
    a=str(i)
    b=str(n-i)
    if a.count('0')==0 and b.count('0')==0:
        result=[i,n-i]
        print(result)
        break