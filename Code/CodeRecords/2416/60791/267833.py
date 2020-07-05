def solve(instr):
    res = 0
    ma = 0
    for i in range(len(instr)-1):
        if(instr[i]%2 != instr[i+1]%2):
            res+=1
        else:
            ma = max(ma,res)
            res = 0
    ma = max(ma,res)
    print(ma+1)
    
    
n,m = [int(i) for i in input().split(' ')]
instr = [0]*n
x = 0
while(x<m):
    instr[int(input())-1] += 1
    solve(instr)
    x+=1
    