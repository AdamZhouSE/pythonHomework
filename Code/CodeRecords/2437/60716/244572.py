move,need = map(int,input().split())
trace = list()
for i in range(move):
    str = input().split(' ')
    if str[1]=='R':
        trace.append(int(str[0]))
    else:
        trace.append(-int(str[0]))
listmodule = list()
location = 0
while len(trace)>0:
    changes = trace.pop(0)
    if changes>=0:
        for i in range(1,changes+1):
            listmodule.append(location+i)
    else:
        for i in range(changes,0):
            listmodule.append(location+i)
    location=location+changes
setmod = set(listmodule)
answersheet = list()
while len(setmod)>0:
    temp = setmod.pop()
    index= 0
    for i in range(len(listmodule)):
        if listmodule[i]==temp:
            index++;
    if index>=need:
        answersheet.append(temp)
print(len(answersheet))