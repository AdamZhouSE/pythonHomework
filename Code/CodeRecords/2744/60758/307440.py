def ishui(a):
    for i in range(0,int(len(a)/2)):
        if a[i]!=a[-i]:
            return False
    return True

get=[]
for _ in range(int(input())):
    x=input().split()
    get.append(x[1])

count=0
for i in range(len(get)):
    for j in range(len(get)):
        if ishui(get[i]+get[j]):
            count+=1
print(count)