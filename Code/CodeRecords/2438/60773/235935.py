list=list(input())
num=(int(len(list))-1)//2
#print(num)
result=[]
for i in range(num):
    result.append(1)
head=0
tail=num-1
for i in range(num):
    #print(2*num+1)
    if list[2*i+1]=='0':
        result[head]=0
        head = head+1
    elif list[2*i+1]=='2':
        result[tail]=2
        tail = tail-1
    else:
        continue
    #print(result)
print(result)
