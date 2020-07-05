inp=input()
start=inp.find('[')
end=inp.find(']')
nums=list(map(int,inp[start+1:end].split(',')))
inp=inp[end:]
k=-1
for i in range(0,len(inp)):
    if inp[i].isdigit():
        temp=i
        while temp<len(inp) and inp[temp].isdigit():
            temp+=1
        k=int(inp[i:temp])
        inp=inp[temp:]
        break
t=-1
for i in range(0,len(inp)):
    if inp[i].isdigit():
        temp=i
        while temp<len(inp) and inp[temp].isdigit():
            temp+=1
        t=int(inp[i:temp])
        break
flag=False
for i in range(0,len(nums)-k):
    for j in range(i+1,i+k+1):
        if abs(nums[i]-nums[j])<=t:
            print("true")
            flag=True
            break
    if flag:
        break
if flag==False:
    print("false")