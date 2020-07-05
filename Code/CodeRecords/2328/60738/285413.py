num_list=list(map(int,input().split(",")))
h=0
m=0
output=""
judge=True
break_flag=0
for i in range(4):
    if num_list[i]==2:
        output+="2"
        del num_list[i]
        break
    elif num_list.count(2)==0:
        if num_list[i]==1:
            output+="1"
            del num_list[i]
            break
    elif num_list.count(1)==0 and num_list.count(2)==0:
        if num_list[i]==0:
            output+="0"
            del num_list[i]
            break
    if i==3:
        judge=False
t=0
if output=="2":
    t=4
else:
    t=10
for j in range(1,t):
    for k in range(3):
        if num_list.count(t-j)==0:
            if j==t:
                judge=False
                break_flag=1
                break
        elif num_list[k]==t-j:
            output+=str(t-j)
            break_flag=1
            del num_list[k]
            break
    if break_flag:
        break
output+=":"
a=min(num_list)
b=max(num_list)
if a>6:
    judge=False
else:
    if b*10+a<=60:
        output+=str(b*10+a)
    else:
        output+=str(a)
        output+=str(b)
if judge:
    print(output)
else:
    print("")
        
    