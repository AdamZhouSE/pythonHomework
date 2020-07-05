num=int(input())
magic=[]
#p=[]
arr=[int(n) for n in input().split(' ')]
for i in range(0,num):
    magic.append(arr[i])
    result=0
    if len(magic)==1:
        result=1
        #p.append(result)
        print(result)
    else:
        re=[]
        for j in range(1,len(magic)+1):
            index=0
            while index+j<=len(magic):
                list=[]
                for k in range(index,index+j):
                      list.append(magic[k])
                if list not in re:
                      re.append(list)
                index=index+1
        result=len(re)
        print(result)
        #p.append(result)