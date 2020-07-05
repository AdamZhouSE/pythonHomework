arr=list(eval(input()))
target=int(input())
l1=[]
l2=[]
for value in range(target//len(arr),max(arr)+1):
    l1.append(value)
    temp=0
    for i in arr:
        if i>value:
            temp+=value
        else:
            temp+=i
    l2.append(abs(target-temp))
print(l1[l2.index(min(l2))])