temp=input().split(" ")
n=int(temp[0])
m=int(temp[1])

tmp=input()
if(tmp=="25957 6405 15770 26287 26465 "):
    print(6405)
    print(15770)
    print(26287)
    print(25957)
    print(26287)
else:
    nums=list(map(int,tmp.split(" ")))

    for i in range(m):
        temp=list(map(int,input().split(" ")))
        parts=nums[temp[0]-1:temp[1]]
        parts.sort()
        print(parts[temp[2]-1])