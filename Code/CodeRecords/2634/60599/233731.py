#来个爆炸长的解法 n2
s=input()
k=int(input())
nums=[]
d = {}

s="".join(s.split(' '))
s="".join(s.split('"'))

l=list(map(int,s[1:len(s)-1].split(',')))
for i in range(0,len(l)-1):
    for t in range(i+1,len(l)):
        nums.append(l[i]/l[t])
        d[l[i]/l[t]]=[l[i],l[t]]
nums.sort()
# print(nums[k-1])
print(d[nums[k-1]])
