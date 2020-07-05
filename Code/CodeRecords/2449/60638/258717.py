numbers=list(map(int,input().split(",")))
n=int(input())
find=False
for i in range(0,len(numbers)):
    if n == numbers[i]:
        find=True
        print(i)
        break
if not find:
    print(-1)