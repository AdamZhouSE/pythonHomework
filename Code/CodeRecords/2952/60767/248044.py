def typewritter(string):
    res = []
    temp = ""
    for s in string:
        if(s=="B"):
            temp = temp[:-1]
        elif(s=="P"):
            res.append(temp)
        else:
            temp = temp+s
    return res

def find(x,y,res):
    a = res[x-1]
    if(y-1>=len(res)):
        return 0
    b = res[y-1]
    cnt = 0
    for i in range(0,len(b)-len(a)+1):
        if(b[i:i+len(a)]==a):
            cnt += 1
    return cnt

string = input()
res = typewritter(string)
#print(res)
num = int(input())
query = []
temp = []
for i in range(0,num):
    temp = input().split(" ")
    temp2 = []
    for t in temp:
        temp2.append(int(t))
    query.append(temp2)
for q in query:
    print(find(q[0],q[1],res))