s=input()
n=int(input())
numStr=""
for i in range(len(s)):
    temp=ord(s[i])-ord('A')+n
    numStr+=str(temp)

num=list(numStr)
num=[int(x) for x in num]

temp=[]
res=""
while len(num)>3:
    for i in range(len(num)-1):
        temp.append((num[i]+num[i+1])%10)
    num=temp
    temp=[]#temp.clear会导致num也变为空！！！！！！！！！！！

if num[0]==1 and num[1]==0 and num[2]==0:
    res="100"
else:
    temp.append((num[0] + num[1]) % 10)
    temp.append((num[1] + num[2]) % 10)
    if temp[0]==0:
        num=temp[1]#此时直接是数字 不是列表！！
        res=str(num)
    else:
        num=temp
        for i in num:
            res+=str(i)
print(res,end="")