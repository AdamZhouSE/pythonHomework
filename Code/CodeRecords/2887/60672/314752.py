def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums

def judge(arr):
    arr=arr[1:]
    answer=''
    if arr[0]>=5:
        answer='LIVE'
    else:
        answer='DEAD'
    return answer

t=int(input())
service=[]
for i in range(t):
    m=input()
    m=nums(m)
    service.append(m)
answer1=[0,0]
answer2=[0,0]
for i in range(len(service)):
    if service[i][0]==1:
        answer=judge(service[i])
        if answer=='LIVE':
            answer1[0]+=1
        else:
            answer1[1]+=1
    if service[i][0]==2:
        answer=judge(service[i])
        if answer=='LIVE':
            answer2[0]+=1
        else:
            answer2[1]+=1
if answer1[0]>=answer1[1]:
    print('LIVE')
else:
    print('DEAD')
if answer2[0]>=answer2[1]:
    print('LIVE')
else:
    print('DEAD')