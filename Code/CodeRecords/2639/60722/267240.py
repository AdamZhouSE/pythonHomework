def most(s):
    num=[]
    for i in range(len(s)):
        num.append(s.count(s[i]))
    return max(num)
s=input()
k=int(input())
result=0
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if j-i+1-most(s[i:j+1])<=k:
            result=max(result,j-i+1)
        else:
            break
print(result)