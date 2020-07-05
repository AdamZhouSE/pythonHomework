def numOf(n):
    if n==1:
        return 3
    else:
        return numOf(n-1)+7+4*(n-2)
    
s=int(input())
for x in range(s):
    print(numOf(int(input())))