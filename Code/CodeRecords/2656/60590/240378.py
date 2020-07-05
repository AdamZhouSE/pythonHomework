t=int(input())
for i in range(t):
    nums=input()
    a=int(nums.split(' ')[0])
    b=int(nums.split(' ')[1])
    if(a==b):
        print(-1)
    abin=str(bin(a))[2:];bbin=str(bin(b))[2:];i=0
    if len(abin)<len(bbin):
        abin='0'*(len(bbin)-len(abin))+abin
    elif len(abin)>len(bbin):
        bbin = '0' * (len(abin) - len(bbin)) + bbin
    while i<len(abin):
        if abin[len(abin)-1-i]!=bbin[len(bbin)-1-i]:
            print(i+1)
            break
        else:
            i+=1
