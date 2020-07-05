num=eval(input())
num.sort()
sub=[]
for i in range(len(num)-1):
    sub.append(num[i+1]-num[i])
print(max(sub))
