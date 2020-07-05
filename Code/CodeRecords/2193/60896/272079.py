n=input()
n=n.split(' ')
m=eval(n[1])
n=eval(n[0])
s=input()

def find_longest_prefix(x,y):
    count=0
    t=min(len(x),len(y))
    for i in range(0,t):
        if(x[i]==y[i]):
            count+=1
        else:return i
    return t

for i in range(0,m):
    count=0
    temp=input()
    temp=temp.split(' ')
    l=eval(temp[0])
    r=eval(temp[1])
    for q in range(l,r+1):
        count2=0
        for t in range(q+1,r+1):
            temp2=0
            str_1=s[:q][::-1]
            str_2=s[:t][::-1]
            count3=find_longest_prefix(str_1,str_2)
            count2=max(count2,count3)
        count=max(count,count2)
    print(count)