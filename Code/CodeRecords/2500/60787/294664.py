a=eval(input())
re=[]
rest=len(a)

def move(n):
    temp=[]
    for i in range(0,n):
        temp.append(a[i])
    temp.reverse()
    for i in range(0,n):
        a[i]=temp[i]

while rest>1:
    max_num=a[0]
    max_index=0
    for i in range(0,rest):
        if a[i]>max_num:
            max_num=a[i]
            max_index=i
    re.append(max_index+1)
    move(max_index+1)
    re.append(rest)
    move(rest)
    rest-=1
print(re)