t=input()
start=t.find('[')
end=t.find(']')
nums=eval(t[start:end+1])
a=t[end+2:].find('=')
b=t[end+2:].find(',')
t=t[end+2:]
k=int(t[a+2:b])
c=t[b+1:].find('=')
t=t[b+1:]
t=int(t[c+2:])
i=0
j=1
leng=len(nums)
flag=False
while i<leng-1:
    j=i+1
    while j<leng and j-i<=k:
        if(abs(nums[j]-nums[i])<=t):
            flag=True
            break
        j+=1
    if(flag):
        break
    i+=1
if(flag):
    print("true")
else:
    print("false")



