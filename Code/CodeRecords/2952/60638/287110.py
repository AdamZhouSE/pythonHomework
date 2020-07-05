string=input()
result=[]
cache=''
for i in range(0,len(string)):
    if string[i]=='B':
        cache=cache[0:-1]
    elif string[i]=='P':
        result.append(cache)
    else:
        cache=cache+string[i]
n=int(input())
for x in range(0,n):
    nums=list(map(int,input().split(" ")))
    a=result[nums[0]-1]
    b = result[nums[1] - 1]
    count=0
    for i in range(0,len(b)):
        find = True
        for m in range(0, len(a)):
            if i + m >= len(b):
                find = False
                break
            if a[m] != b[i + m]:
                find = False
        if find:
            count = count + 1
    print(count)