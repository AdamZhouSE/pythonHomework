num_list=list(map(int,input().split(",")))
one=0
two=0
length=len(num_list)
for i in range(length-1):
    if num_list[i]>num_list[i+1]:
        two+=1
for i in range(length-1):
    for j in range(i+1,length-1):
        if num_list[i]>num_list[j]:
            one+=1
if one==two:
    print(True)
else:
    print(False)