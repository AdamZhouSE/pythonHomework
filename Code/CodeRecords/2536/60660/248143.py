import re,collections
def findItinerary(tickets):
    dic = collections.defaultdict(list)  # 邻接表
    for ori, des in tickets:
        dic[ori] += [des]  # 路径存进邻接表
    for ori in dic:
        dic[ori].sort()  # 邻接表排序
    ans = []

    def dfs(f):  # 深搜函数
        while dic[f]:
            dfs(dic[f].pop(0))  # 路径检索
        ans.insert(0, f)  # 放在最前

    dfs('JFK')
    return ans

inlist=re.sub("[\[\]\"\ ]","",input()).split(",")
tickets=[]
for i in range(0,len(inlist),2):
    tickets.append([inlist[i],inlist[i+1]])
print(str(findItinerary(tickets)))
