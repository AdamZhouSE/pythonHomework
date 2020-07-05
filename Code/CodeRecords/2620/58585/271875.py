def power(n):
    output=0
    for i in range(1,n+1):
        output+=pow(i,5)
    return output

num=int(input())
for i in range(num):
    n=int(input())
    print(power(n))