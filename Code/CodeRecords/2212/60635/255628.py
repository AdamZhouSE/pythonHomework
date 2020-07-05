count=int(input())
def caldivsum(src):
    sum=0
    for i in range(1,src+1):
        if src%i==0:
            sum+=i
    return sum
for i in range(count):
    src=int(input())
    if caldivsum(src)<2*src:
        print(1)
    else:
        print(0)