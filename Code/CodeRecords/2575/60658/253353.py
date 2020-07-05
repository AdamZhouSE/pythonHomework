li = input()
ans = [0]*len(li)
for i in range(1,len(li)):
    if li[i]==li[i-1]:
        ans[i]=1-ans[i-1]
    else:
        ans[i]=ans[i-1]
print(ans)