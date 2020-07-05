str1=[[1],[2],[4],[8],[1,6],[3,2],[6,4],[1,2,8],[2,5,6],[1,2,5],[0,1,2,4],[0,2,4,8]]

n = input()
list = list(set(n))
for i in range(0,len(list)):
    list[i]=int(list[i])
result = False
for i in range(0,len(str1)):
    if list == str1[i]:
        result=True
        break
        
print(result)