front=int(input())
behind=int(input())
result=[]
for num in range(front, behind+1):
    allDone=True
    for item in str(num):
        try:
            if num%(int(item))!=0:
                allDone=False
                break
        except:    # 10 20之类的
            allDone=False
            break
    if allDone:
        result.append(num)
print(result)
