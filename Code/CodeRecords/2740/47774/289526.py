times=input().replace('[','').replace(']','').replace('"','').split(',')#格式化输入
res=[]
#转为分钟
for time in times:
    num = int(time[0:2])*60+int(time[3:5])
    res.append(num)
res.sort()#排序
#依次作减
ans=res[0]+24*60-res[-1]#头和尾没能循环到，补上
for i in range(1,len(res)):
    ans=min(ans,res[i]-res[i-1])
print(ans)
