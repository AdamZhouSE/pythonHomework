cmd = [int(n) for n in input().split( )]
num = cmd[0]
k = cmd[1]
arr = ['']*num
count = num
while count:
    s = input().split( )
    mom = int(s[1])-1
    if mom == -1:
        arr[0] = s[0]
    else:
        arr[num-count] = s[0]+arr[mom]
    count -= 1
while k:
    strs = input()
    ans = 0
    for j in arr:
        if j.startswith(strs):
            ans+=1
    print(ans)
    k -= 1
    