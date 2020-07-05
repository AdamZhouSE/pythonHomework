class Function:
    def schedule(self, startTime, endTime, profit):
        length = len(startTime)
        times = [[0, 0, 0] for _ in range(length)]
        for i in range(length):
            times[i][0] = startTime[i]
            times[i][1] = endTime[i]
            times[i][2] = profit[i]
        times.sort() 
                
        dp = [0 for i in range(length)]
        
        res = 0
        s = 0
        pos = 0
        for i in range(length):
            for j in range(pos, i):
                if times[i][0] >= times[j][1]:
                    if j == pos:
                        pos += 1
                    s = max(s, dp[j])
            dp[i] = s + times[i][2]
            res = max(res, dp[i])
                              
        return res

s1=input().split(",")
s2=input().split(",")
s3=input().split(",")
list1=[]
list2=[]
list3=[]
for i in range(len(s1)):
    list1.append(int(s1[i]))
    list2.append(int(s2[i]))
    list3.append(int(s3[i]))
s=Function()
ans=s.schedule(list1,list2,list3)
print(ans)
