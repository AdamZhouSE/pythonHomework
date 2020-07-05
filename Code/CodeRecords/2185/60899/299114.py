numOftests = int(input())
for i in range(numOftests):
    n = int(input())
    exo = 0
    for k in range(1,10000):
        if 2**k-1<=n and 2**(k+1)-2>=n:
           exo = k
           break
    n10 = n -2**k+1
    n2 = bin(n10)
    str0 = n2[2:]
    str1 = str0.replace("0","4").replace("1","7")
    str2 = "4"*(k-len(str1))+str1
    print(str2)