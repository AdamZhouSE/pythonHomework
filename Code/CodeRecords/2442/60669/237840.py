list=eval(input())
list=sorted(list)

diff=0
for i in range(0,len(list)-1):
    temp=abs(list[i]-list[i+1])
    if temp>diff:
        diff=temp
print(diff)