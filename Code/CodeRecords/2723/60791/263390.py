def solve(s):
    if(len(s)==1):
        print(s)
        return
    else:
        temp = 0
        for item in list(s):
            temp += int(item)
        solve(str(temp))
        return

T = int(input())
x = 0
while(x < T):
    x += 1
    solve(input())
    