strs = input().split(',')
lists = [int(i) for i in strs]
answer = list()
for i in range(len(lists)-2):
    for j in range(i,len(lists)-1):
        for k in range(j+1,len(lists)):
            temp = list()
            temp.append(lists[i])
            temp.append(lists[j])
            temp.append(lists[k])
            temp.sort()
            if temp[0]+temp[1]>temp[2]:
                answer.append(lists[i]+lists[j]+lists[k])
answer.sort()
answer.reverse()
if len(answer)==0:
    print("0")
else:
    print(answer[0])