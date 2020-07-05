num=int(input())
lst=input().split()
lst=list(map(int,lst))
ans=[]
for i in range(num-1):
    ans.append(str(lst[i]+lst[i+1]))
ans.append(str(lst[-1]))
print(str(" ".join(ans)))