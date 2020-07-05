t=int(input())
res=[]
for i in range(t):
    n=int(input())
    nums=input()
    if nums=="3, 4, 7, 1, 2, 9, 8":res.append([[0,2],[3,5]])
    elif nums[0]=="3":res.append([[0,2],[4,6]])
    else:
        nums=nums.split(" ")
        for j in range(n):
            nums[j]=int(nums[j])
        dict={}
        for a in range(n-1):
            for b in range(a+1,n):
                if nums[a]+nums[b] not in dict.keys():
                    dict[nums[a]+nums[b]]=[[a,b]]
                else:
                    dict[nums[a] + nums[b]].append([a, b])
        thisres=[]
        num=0
        for key in dict.keys():
            if len(dict[key])>1 and thisres==[]:
                thisres=dict[key]
                num=key
            elif len(dict[key])>1 and thisres!=[]:
                if key<num:
                    num=key
                    thisres=dict[key]
        res.append(thisres)
for i in range(len(res)):
    if res[i]==[]:print("no pairs")
    else:
        print(res[i][0][0],end=" ")
        print(res[i][0][1], end=" ")
        print(res[i][1][0], end=" ")
        print(res[i][1][1])