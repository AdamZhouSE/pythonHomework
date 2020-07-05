def getLocation(str,P):
    temp = pow(32,2)*(ord(str[-3])-65)+pow(32,1)*(ord(str[-2])-65)+(ord(str[-1])-65)
    return temp%P

P = int(input().split()[1])
nums = [i for i in input().split()]
middle = [0] * P
out = []

for i in range(len(nums)):
    loc = getLocation(nums[i],P)
    if(middle[loc]==0):
        middle[loc] = 1
        out.append(loc)
    else:
        n = 1
        while(middle[loc]!=0):
            loc = (loc+n*n)%P
            n+=1
        middle[loc] = 1
        out.append(loc)
print(nums,P)
print("".join( [str(out[i])+' ' for i in range(len(out))]) )