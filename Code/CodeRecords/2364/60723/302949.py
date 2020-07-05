def judge(number):
    string=list(str(number))
    string.sort()
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            return True
    return False
ans=0
num=int(input())
for i in range(num+1):
    if judge(i):
        ans=ans+1
print(ans)