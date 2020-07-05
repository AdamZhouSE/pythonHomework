number=int(input())
details=list(map(int, input().split()))
print(details.count(1))
for i in range(0,len(details)-1):
    if details[i]>=details[i+1]:
        print(details[i],end='')
        print(" ",end='')
print(details[number-1]) 