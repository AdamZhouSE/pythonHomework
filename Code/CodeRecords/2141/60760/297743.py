def func(n:int):
    result=[]
    for i in range(1,n+1):
        res=''
        while i>=1:
            res=res+str(i%2)
            i=int(i/2)
        result.append(res[::-1])
    for i in range(len(result)):
        print(result[i],end=" ")
    print()
    return 0
tests = int(input())  # 找律
lists = []
for i in range(tests):
    lists.append(int(input()))
for i in lists:
    func(i)