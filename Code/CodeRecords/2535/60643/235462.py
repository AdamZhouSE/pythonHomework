data=input()
#处理输入格式
sortedInp=sorted(data)
cnt=0
for i in range(1,len(data)+1):
    if max(data[0:i])==i-1:
        cnt+=1
print(cnt)