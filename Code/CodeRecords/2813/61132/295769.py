n=int(input())
dic={}
Max=0
winner=''
for i in range(n):
    tmp=list(input().split())
    if dic.get(tmp[0],'x') != 'x':
        dic[tmp[0]]+=int(tmp[1])
    else:
        dic[tmp[0]]=int(tmp[1])
    if dic[tmp[0]] > Max:
        winner = tmp[0]
        Max = dic[tmp[0]]
print(winner)