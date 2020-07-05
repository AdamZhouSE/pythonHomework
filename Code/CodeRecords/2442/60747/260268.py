num=eval(input())
num.sort()
sub=[]
for i in range(len(num)-1):num=eval(input())
num.sort()
sub=[]
for i in range(len(num)-1):
    sub.append(num[i+1]-num[i])
if len(sub)==0:
    print(0)
else:
    print(max(sub))

    sub.append(num[i+1]-num[i])
print(max(sub))
