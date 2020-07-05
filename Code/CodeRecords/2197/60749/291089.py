def find(nums):
    peoples=[True for _ in range(nums)]
    result=[]
    num=1
    call=2
    while any(peoples):
        for index, people in enumerate(peoples):
            if people:
                if num==call:
                    peoples[index]=False
                    result.append(index+1)
                    num=1
                else:
                    num+=1
    return result[-1]
res=[]
ans=[]
n=int(input())
for _ in range(n):
    ans.append(int(input()))
for h in ans:
    res.append(find(h))
for t in res:
    print(t)