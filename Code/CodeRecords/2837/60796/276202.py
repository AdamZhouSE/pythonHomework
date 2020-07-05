nums=input().split(" ")
N=int(nums[0])
l=int(nums[1])
r=int(nums[2])

can=[1]
for i in range(1,N):
    can.append(pow(2,i))

min=can[:l]
while len(min)<N:
    min.append(1)

max=can[:r]
while len(max)<N:
    max.append(can[r-1])

s1=0
s2=0
for i in range(N):
    s1=s1+min[i]
    s2=s2+max[i]
print(s1,s2)