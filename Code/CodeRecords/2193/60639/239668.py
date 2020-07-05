inp = input().split(' ')
m = int(inp[1])
Str = input()
for i in range(0,m):
    list = input().split(' ')
    l = int(list[0])
    r = int(list[1])
    subStr=Str[l-1:r]
    leng=r-l+1
    list=[[] for j in range(leng)]
    for k in range(leng):
        for m in range(k+1):
            list[k].append(subStr[m])
    count=[]
    nums=[]
    for a in range(0,leng-1):
        for b in range(a+1,leng):
            num = 0
            for c in range(0,a+1):
                if list[a][a-c]==list[b][b-c]:
                    num=num+1
                else:
                    break
            nums.append(num)
        count.append(max(nums))
    output=max(count)
    print(output)



