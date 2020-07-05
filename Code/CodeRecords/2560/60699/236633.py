cnt=int(input())
for i in range(0,cnt):
    k=int(input())
    arr=input()
    arr=list(map(int,arr.split(' ')))
    t=int(input())
    dict1={}
    for j in arr:
        dict1[j]=dict1.get(j,0)+1
    sorted_key_list=[]
    for j in dict1:
        sorted_key_list.append(dict1[j])
    sorted_key_list.sort()
    for m in range(0,len(sorted_key_list)):
        if t>=sorted_key_list[m]:
            t-=sorted_key_list[m]
            sorted_key_list[m]=0
        else:
            break
    res=0
    for j in sorted_key_list:
        if j!=0:
            res+=1
    print(res)