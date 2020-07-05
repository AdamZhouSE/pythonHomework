numOftests = int(input())
for i in range(numOftests):
    n = int(input())
    ans = ""
    for j in range(1,n):
        s = str(bin(j))[2:]
        ans+= s+" "
    ans += str(bin(n))[2:]+" "
    print(ans)