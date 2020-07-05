# size=int(input())
# lst=[]
# by=[]
# n=0
# def tr(num,flag,time):
#     maxn=0
#     for i in range(num):
#         if flag==1:
#             if len(by[i])>=time-1:
#                 maxn=max(lst[num]-lst[i]+by[i][time-1][0],maxn)
#     if flag==0:
#         maxn=max(by[num-1][time][1],by[num-1][time][0])
#     return maxn
#
#
# for k in range(size):
#     tot=int(input())
#     n=int(input())
#     by=[[]for m in range(n)]
#     lst=input().split()
#     lst=[int(x) for x in lst]
#     by[0].append([0,0])
#     for i in range(1,n):
#         by[i].append([0,0])
#         maxj=0
#         print(by)
#         for j in range(len(by[i-1])-1):
#             maxj = j
#             list1=[0,0]
#             if j>=tot:
#                 break
#             else:
#                 list1[1]=tr(i,1,j)
#                 list1[0]=tr(i,0,j)
#                 by[i].append(list1)
#         if len(by[i-1][maxj])>=2:
#             list1=[0,tr(i,1,maxj+1)]
#             by[i].append(list1)
#     maxr=0
#     for i in range(n):
#         if len(by[i])>=tot:
#             maxr=max(maxr,by[i][tot][0],by[i][tot][1])
#     print(maxr)

t=int(input())
while(t>0):
    t-=1
    k=int(input())
    n=int(input())
    arr=input().split()
    arr=list(map(int,arr))
    dp=[[0 for i in range(k+1)]for j in range(n+1)]
    for i in range(2,n+1):
        for j in range(1, k+1):
            dp[i][j]=dp[i-1][j]
            for p in range(1,i): dp[i][j]=max(dp[i][j],dp[p-1][j-1]+arr[i-1]-arr[p-1])
    print(dp[n][k])