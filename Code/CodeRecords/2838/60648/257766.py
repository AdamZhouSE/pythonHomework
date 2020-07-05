#将正整数读入数组中排序，第一个和最后一个，依次相加
n=input()
n=int(n)
ls=input().split(' ')
#print(ls)
ls=[int(ls[i]) for i in range(n)]
ls.sort()
#print(ls)
r=0
for i in range(n/2):
    r+=(ls[i]+ls[n-1-i])**2
print(r)
    