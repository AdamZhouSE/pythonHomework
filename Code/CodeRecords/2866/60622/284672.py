n=int(input())
arr=input().split()
while arr[0]!='1':
    arr.pop(0)
while arr[-1]!='1':
    arr.pop()
index=0
ans=[]
if len(arr)==1 and arr[0]=='1':
    ans.append(1)
else:
    while index < len(arr) - 1:
        if arr[index] == '1' and arr[index + 1] == '0':
            count = 0
            while arr[index + 1] != '1':
                count += 1
                index += 1
            index += 1
            ans.append(count + 1)
        else:
            index += 1

a=1
for n in ans:
    a=a*n
print(a)