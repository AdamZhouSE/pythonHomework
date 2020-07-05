arr=eval(input())
candi_a=arr[0]
candi_b=0
count_a=0
count_b=0
for i in arr:
    if i==candi_a:
        count_a+=1
        continue
    if i==candi_b:
        count_b+=1
        continue
    if count_a==0:
        candi_a=i
        count_a+=1
    elif count_b==0:
        candi_b=i
        count_b+=1
    else:
        count_a-=1
        count_b-=1
count_a=0
count_b=0
for i in arr:
    if i==candi_a:
        count_a+=1
    elif i==candi_b:
        count_b+=1
res=[]
if count_a>len(arr)//3:
    res.append(candi_a)
if count_b>len(arr)//3:
    res.append(candi_b)
print(res)
