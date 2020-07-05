def generate(k, n):
    if k == (n//2)+1:
        return "D"*n
    else:
        star = abs(n+1-2*k)//2
        p = "*"*star+"D"*(n-2*star)+"*"*star
        return p


num = int(input())
for i in range(1, num+1):
    print(generate(i, num))