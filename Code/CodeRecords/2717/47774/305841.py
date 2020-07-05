equations=eval(input())
flag='true'
nums={chr(i): chr(i) for i in range(97, 125)}
        
def find(x):
    if x != nums[x]:
        nums[x]= find(nums[x])
    return nums[x]

for eq in equations:  
    if eq[1]=='=':
        nums[find(eq[0])]= find(eq[-1])

for eq in equations:
    if eq[1]=='!':
        if find(eq[0]) == find(eq[-1]):
            flag='false'
            break
print(flag)