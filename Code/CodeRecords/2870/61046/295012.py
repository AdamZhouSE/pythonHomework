num=int(input())
test=input().split()
test=sorted(list(map(int ,test)))

ans=sum(test)
if ans%2==0:
    print(ans)
else:
    for x in test:
        ans-=x
        if ans%2==0:
            print(ans)
            break