def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums

n=int(input())
square=[[0,0] for i in range(n)]
for i in range(n):
    string=nums(input())
    square[i]=string
answer='YES'
height=[max(square[0][0],square[0][1])]
indicate=0
for i in range(n-1):
    if square[i+1][0]<=height[i]:
        if square[i+1][1]<=height[i]:
            height.append(max(square[i+1][0],square[i+1][1]))
        else:
            height.append(square[i+1][0])
    elif square[i+1][1]<=height[i]:
        height.append(square[i+1][1])
    else:
        break
if len(height)<n:
    print('NO')
else:
    print('YES')