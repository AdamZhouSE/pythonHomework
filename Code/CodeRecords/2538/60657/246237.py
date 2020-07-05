num=input()
num=num[1:-1]
num=num.split(',')
num=[int(i) for i in num]
num.sort()
cons=num[-1]+1
if num[0]>1:
    cons=1
else:
    for i in range(len(num)-1):
        if num[i+1]-num[i]>1:
            cons=num[i]+1
            if cons>0:
                break
print(cons)


