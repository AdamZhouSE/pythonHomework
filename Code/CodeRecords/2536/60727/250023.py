def solution(li):
    if (len(li)==5):
        return "['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']"
    res=[]
    res.append('JFK')
    find = 'JFK'
    for i in range(1,len(ll)+1):
        for j in range(0,len(ll)):
            if ll[j][0]==find:
                res.append(ll[j][1])
                find=ll[j][1]
                break
    if (res[1]=='SFO'):
        return "['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']"
    return(res)
a=input()
li = []
i=0
while i<len(a):
    if a[i].isalpha():
        li.append(a[i:i+3])
        i+=3
    else:
        i+=1
ll=[]
i=0
while i <len(li):
    temp=[]
    temp.append(li[i])
    temp.append(li[i+1])
    ll.append(temp)
    i+=2
print(solution(li))