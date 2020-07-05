x=int(input())

def swapInt(num,count):
    if num==1:
        return count
    if num%2==0:
        return swapInt(num/2,count+1)
    return min(swapInt(num-1,count+1),swapInt(num+1,count+1))

print(swapInt(x,0))
