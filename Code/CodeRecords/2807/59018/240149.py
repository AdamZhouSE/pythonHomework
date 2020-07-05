n,m=input().split(' ')
info1=input().split(' ')
a=[int(x) for x in info1]
info2=input().split(' ')
b=[int(y) for y in info2]


count_a_even=0                            #even偶数 odd奇数
count_a_odd=0
for i in range(n):
    if a[i]%2==0:
        count_a_even=count_a_even+1
count_a_odd=n-count_a_even

count_b_even=0                            #even偶数 odd奇数
count_b_odd=0
for j in range(m):
    if b[j]%2==0:
        count_b_even=count_b_even+1
count_b_odd=m-count_b_even


print(min(count_a_odd,count_b_even)+min(count_a_even,count_b_odd))
        
        