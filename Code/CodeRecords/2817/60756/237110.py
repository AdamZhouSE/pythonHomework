firstLine=input()
n=int(firstLine)
secondLine=input().split()
for i in range(n):
    one=int(secondLine[i])-1
    two=int(secondLine[one])-1
    three=int(secondLine[two])-1
    if three==i:
        print("YES")
        break
    if i==n-1:
        print("NO")