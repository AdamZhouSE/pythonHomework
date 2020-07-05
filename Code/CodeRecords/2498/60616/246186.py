nums=eval(input())
odd=[]
even=[]
for num in nums:
    if(num%2==1):odd.append(num)
    else:even.append(num)
ans=[]
half=len(odd)
for i in range(half):
    ans.append(even[i])
    ans.append(odd[i])
print(ans)