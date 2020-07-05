num=int(input())
for i in range(num):
    string=input()
    s=list(set(string))
    count=[]
    for j in s:
        count.append(string.count(j))
    flag=1
    for j in count:
        if j>1:
            flag=0
            break
    if flag==1:
        print(-1)
    else:
        dis=0
        for j in range(len(count)):
            if count[j]>1:
                pos1=string.index(s[j])
                string=string[::-1]
                pos2=string.index(s[j])
                string=string[::-1]
                dis=max(dis,len(string)-pos1-pos2-2)
        print(dis)