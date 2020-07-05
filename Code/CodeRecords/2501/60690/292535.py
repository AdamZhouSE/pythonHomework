n=int(input())
before=input().split(" ")
later=input().split(" ")
res=0
for i in range(len(before)-1):
    for j in range(i+1,len(before)):
        if later.index(before[i])>later.index(before[j]):
            res+=1
print(res)