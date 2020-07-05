n = int(input())
computers = [[]*2]*n
for i in range(n):
    computers[i] = list(map(int,input().split()))
for i in range(n-1):
    Find = False
    for j in range(i,n):
        if computers[j][0]<computers[i][0] and computers[j][1]>computers[i][1] or
        computers[i][0]<computers[j][0] and computers[i][1]>computers[j][1]:
            Find =True
            break
    if Find:
        break
print("Happy Alex" if Find else "Poor Alex")
        
    
