arr=input()
num=int(input())
cons=[]
for i in range(num):
    cons.append(input().split(' '))

def cal(all):
    pr=[]
    string=''
    for i in range(len(all)):
        if all[i]=='P':
            pr.append(string)
            string += ''
        elif all[i]=='B':
            string=string[0:-1]
        else:
            string+=all[i]

    return pr

con=cal(arr)
final=[]
for i in range(len(cons)):
    a=int(cons[i][1])-1
    b=int(cons[i][0])-1
    final.append(con[a].count(con[b]))
for k in final:
    print(k)