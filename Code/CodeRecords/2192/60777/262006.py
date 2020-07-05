t=int(input())

for i in range(t):
    start=int(input())
    print(start,end=' ')
    temp=start-5
    while(temp>0):
        print(temp,end=' ')
        temp-=5
    while(temp!=start):
        print(temp,end=' ')
        temp+=5
    print(start,end=' ')
    print()