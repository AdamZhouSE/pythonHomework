def cal_contribution(s,t,w1,w2):
    length=0
    for i in range(min(len(s),len(t))):
        if list(s)[i]==list(t)[i]:
            length+=1
        else:
            break
    return length+w1^w2

a=int(input().strip())
s=input().strip()
weight=[int(x) for x in input().strip().split()]
m=0
for i in range(a-1):
    for j in range(i+1,a):
        if cal_contribution(s[i:],s[j:],weight[i],weight[j])>m:
            m= cal_contribution(s[i:],s[j:],weight[i],weight[j])
print(m)
    