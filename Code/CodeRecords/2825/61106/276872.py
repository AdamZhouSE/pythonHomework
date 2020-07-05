num=int(input())
grade=sum(map(int,input().split()))
all=[grade]
while(num>1):
    all.append(sum(map(int,input().split())))
    num -=1
all.sort()
all.reverse()
print(all.index(grade)+1)