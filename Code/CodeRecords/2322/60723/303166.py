def judge(num):
    if num<=3:
        return True
    string1=str(num)
    string2=str(int(num**2))
    if string1[::-1]==string1 and string2[::-1]==string2:
        return True
    return False
L=int(input())
R=int(input())
left=int(L**0.5)
right=int(R**0.5)+1
ans=0
for i in range(left,right+1):
    if L <= i**2 <= R and judge(i):
        ans=ans+1
print(ans)