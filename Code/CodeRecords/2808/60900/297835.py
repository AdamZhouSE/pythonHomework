
n = int(input())
s = input().split(' ')
for i in range(0,n):
    s[i] =int(s[i])
maxindex = s.index(max(s))
minindex = s.index(min(s))
max1 = max(maxindex,n-1-maxindex)
max2 = max(minindex,n-1-minindex)
print(max(max1,max2))