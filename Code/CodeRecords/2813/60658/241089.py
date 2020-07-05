n = int(input())
dic = {}
m = 0
winner = ""
for i in range(n):
    name,score = input().split()
    score = int(score)
    if name in dic:
        dic[name]+=score
    else:
        dic[name]=score
    if dic[name]>m:
        winner=name
        m=dic[name]

print(winner)
    
    