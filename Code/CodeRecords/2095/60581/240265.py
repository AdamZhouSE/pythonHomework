import sys

lst = []
for line in sys.stdin:
    if line.strip()=='':
        break
    lst.append(line)

list1 = []
for i in range(0,len(lst[0])):
    if lst[0][i] == '0':
        list1.insert(0,0)
    elif lst[0][i]=='1':
        list1.insert(0,1)

list2 = []
for i in range(0,len(lst[1])):
    if lst[1][i] == '0':
        list2.insert(0,0)
    elif lst[1][i] == '1':
        list2.insert(0,1)

forward = 0

answer = []
while len(list2)<len(list1):
    list2.append(0)
while len(list1)<len(list2):
    list1.append(0)

for i in range(0,len(list1)):
    if list1[i]==0 and list2[i]==0 and forward==0:
        answer.append('0')
    elif list1[i]==0 and list2[i]==0 and forward==1:
        answer.append('1')
        forward = 0
    elif (list1[i]==1 or list2[i]==1) and (list1[i]==0 or list2[i]==0) and forward==0:
        answer.append('1')
    elif (list1[i] == 1 or list2[i] == 1) and (list1[i] == 0 or list2[i] == 0) and forward == 1:
        answer.append('0')
    elif list1[i]==1 and list2[i]==1 and forward==0:
        answer.append('0')
        forward = 1
    elif list1[i]==1 and list2[i]==1 and forward==1:
        answer.append('1')

if forward==1:
    answer.append('1')

outPut = ''
for i in range(0,len(answer)):
    outPut += answer[len(answer)-i-1]

print(outPut)



