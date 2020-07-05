num=[int(i) for i in input().split(",")]
num=sorted(num)
num.reverse()
re=0
for i in range(0,len(num)-2):
    if num[i]<num[i+1]+num[i+2]:
        re=num[i]+num[i+1]+num[i+2]
print(re)