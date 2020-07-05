def overtake_cars(before,after:list,n):
    res=0
    for i in range(n-1,0,-1):
        for j in range(i-1,-1,-1):
            if after.index(before[i])<after.index((before[j])):
                res+=1
                break
    return res

n=int(input())
before=list(map(int,input().split()))
after=list(map(int,input().split()))
print(overtake_cars(before,after,n))