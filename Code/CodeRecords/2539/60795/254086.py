arr=input()
newarr=""
for i in range(1,len(arr)-1):
    newarr=newarr+arr[i]
list=[int(n) for n in newarr.split(',')]
large=0
re=[]
for i in range(1,len(list)):
    if list[i]>list[i-1]:
        large=i
    else:
        re.append(list[i-1])
        re.append(list[i])
        break
max=list[large]
pos=large+2
for i in range(large+2,len(list)):
    if list[i]>max:
        max=list[i]
    else:
        for j in range(pos,i+1):
            re.append(list[j])
        pos=i+1
print(len(re))
