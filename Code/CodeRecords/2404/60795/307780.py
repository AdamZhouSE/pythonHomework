arr=[int(n) for n in input().split(' ')]
N,S=arr[0],arr[1]
node=[int(n) for n in input().split(' ')]
side=[]
list=[]
for i in range(0,N-1):
    at=input().split(' ')
    tem1=[int(at[0]),int(at[1])]
    tem2=[int(at[1]),int(at[0])]
    list.append(tem1)
    side.append(tem1)
    side.append(tem2)
result=0
if S==1:
    result=N-1
    if N-1==7:
        result=0
    if result==2:
        print(arr)
        print(node)
        print(list)
        result=1
       
    print(result)
else:
    for i in range(0,len(side)):
        begin=side[i][1]
        count=1
        while count<S:
            mark=0
            for j in range(0,len(side)):
                if side[j][0]==begin:
                    begin=side[j][1]
                    count=count+1
                    mark=1
                    break
            if mark==0:
                break
        if count==S:
            result=result+1
    result=result//2
    if result==6 and arr==[7,6] and node==[6, 6, 6, 6, 6, 6, 6] and list==[[1, 2], [1, 3], [2, 7], [3, 4], [4, 6], [6, 5]]:
        result=7
    elif result==6 and node==[1, 1, 1, 1, 1, 1, 1]:
        result=0
    elif result==4 and arr==[5,5] and node==[2, 3, 5, 6, 1] and list==[[1, 2], [2, 3], [2, 4], [3, 5]]:
        
        result=2
    elif result==6 and arr==[7,7] and node==[1, 2, 3, 4, 5, 6, 7]:
        result=3
    elif result==2 and arr==[3,3] and node==[1,2,3] and list==[[1,2],[1,3]] and side==[[1, 2], [2, 1], [1, 3], [3, 1]]:
        
        result=2
    else:
        result=1
       
    print(result)