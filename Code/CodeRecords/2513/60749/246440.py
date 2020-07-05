n=int(input())
res=[]

for x in range(0,n):
    res.append(input())
k=int(input())
def findsquarenumber(num):
    i=1
    while num>=i*i:
        if num<(i+1)*(i+1):
            return i
        i+=1
squarenumber=findsquarenumber(k)
target_num=k-squarenumber*squarenumber
if target_num==0:
    print(res[squarenumber-1][squarenumber-1])
else:
    target_num_array=[]
    for t in range(0,squarenumber+1):
        target_num_array.append(res[squarenumber][t])
    for t in range(0,squarenumber):
        target_num_array.append(res[t][squarenumber])
    target_num_array=sorted(target_num_array)
    print(target_num_array[target_num-1])




