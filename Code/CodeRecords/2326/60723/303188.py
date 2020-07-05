def judge(p1,p2,p3):
    n1=int(p1,2)
    n2=int(p2,2)
    n3=int(p3,2)
    if n1==n2 and n2==n3:
        return True
    return False
temp=input().split(',')
string=''
flag=False
for i in range(len(temp)):
    string=string+str(temp[i])
for i in range(len(string)-3):
    for j in range(i+3,len(string)):
        part1=string[:i+1]
        part2=string[i+1:j]
        part3=string[j:]
        if judge(part1,part2,part3):
            ans=[i,j]
            flag=True
            break
    if flag:
        break
if flag:
    print(ans)
else:
    print('[-1, -1]')