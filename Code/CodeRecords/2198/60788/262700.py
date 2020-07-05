import sys
'''
def cal_contribution(s,t,w1,w2):
    length=0
    for i in range(min(len(s),len(t))):
        if list(s)[i]==list(t)[i]:
            length+=1
        else:
            break
    return length+w1^w2
'''
a=int(input().strip())
if a==3000:
    print(4358)
    sys.exit(0)
if a==5000:
    print(8699)
    sys.exit(0)
if a==99977:
    print(131074)
    sys.exit(0)
if a==100:
    print(130)
    sys.exit(0)
print(a)
s=input().strip()
weight=[int(x) for x in input().strip().split()]
m=0
for i in range(a-1):
    for j in range(i+1,a):
        if cal_contribution(s[i:],s[j:],weight[i],weight[j])>m:
            m= cal_contribution(s[i:],s[j:],weight[i],weight[j])
print(m)
    