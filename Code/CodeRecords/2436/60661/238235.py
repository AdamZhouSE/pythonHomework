lists=list(input().split('],['))
lists[0]=lists[0][2:];lists[len(lists)-1]=lists[len(lists)-1][:-2]
add=input()[1:-1].split(',')
nums=[]
for k in range(len(lists)):
    num1 = int(lists[k][:lists[k].index(',')])
    num2 = int(lists[k][lists[k].index(',') + 1:])
    nums.append(num1);nums.append(num2)
for l in range(0,len(nums),2):
    if int(add[0])<nums[l] and l!=0:
        nums.insert(l,int(add[1]))
        nums.insert(l,int(add[0]))
        break
res=[]
for i in range(0,len(nums),2):
    num1=nums[i];num2=nums[i+1]
    if len(res)==0:
        res.append(num1);res.append(num2)
        continue
    insert=False
    for j in range(1,len(res),2):
        if num1<=res[j] and num2>res[j]:
            res[j]=num2
            insert=True
            break
        elif num1>=res[j-1] and num2<=res[j]:
            insert=True
    if not insert:
        res.append(num1);res.append(num2)
pri=[]
for k in range(0,len(res),2):
    pri.append([res[k],res[k+1]])
print(pri)
