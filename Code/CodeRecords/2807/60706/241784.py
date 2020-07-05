list=input().split(' ')
n=int(list[0])
m=int(list[1])
case=input().split(' ')
key=input().split(' ')
count=0
ans=0
case_odd=int(0)
case_even=int(0)
for i in range(n):
    if int(case[i])%2==1:
        case_odd=case_odd+1
    else:
        case_even=case_even+1
key_odd=int(0)
key_even=int(0)
for i in range(m):
    if int(key[i])%2==1:
        key_odd=key_odd+1
    else:
        key_even=key_even+1
ans1=0
ans2=0
if key_odd>case_even:
    ans1=case_even
else:
    ans1=key_odd
if key_even>case_odd:
    ans2=case_odd
else:
    ans2=key_even
print(ans1+ans2)