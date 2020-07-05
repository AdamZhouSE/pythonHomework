n=int(input())
arr = [int(x) for x in input().split(" ")]
ans=[]
for i in arr:
    if ans.count(i)==0:ans.append(i)
    else:
        ans.remove(i)
        ans.append(i)
print(len(ans))
print(" ".join([str(x) for x in ans]))