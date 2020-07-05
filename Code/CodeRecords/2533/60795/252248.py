newarr=input()
arr=""
for i in range(1,len(newarr)-1):
    arr=arr+newarr[i]
list=[int(n) for n in arr.split(',')]
re=[]
for i in range(0,len(list)):
    if list[i]%2==0:
        re.insert(0,list[i])
    else:
        re.append(list[i])
print(re)