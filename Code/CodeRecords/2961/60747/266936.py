s=input()
arr=[]
arr.append(s)
for i in range(1,len(s)):
    arr.append(s[i:]+s[0:i])
arr.sort()
result=''
for i in range(len(s)):
    result = result + arr[i][len(s)-1]
print(result,end='')