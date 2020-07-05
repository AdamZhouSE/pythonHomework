n = int(input())
nums =[]
for i in range(0,n):
    nums.append(int(input()))

for i in range(0,n):
    a = nums[i]
    result =""
    result+=str(a%9)
    for j in range(0,int(a/9)):
        result+="9"
    for j in range(0,a):
        result+="0"
    print(result)
