length=int(input())
pages=[int(x) for x in input().split()]
days=0
end=0
for i in range(length):
    end=max(pages[i]-1,end)
    if i==end:
        days+=1
print(days)