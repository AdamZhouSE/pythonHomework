n=int(input())
dict={}
list=[]
store=[]

for i in range(n):
    s=input().split(" ")
    store.append(s)
    if s[0] not in dict.keys():
        dict[s[0]]=len(list)
        list.append(int(s[1]))
    else:
        list[dict[s[0]]]+=int(s[1])
m=max(list)
winner=""
dict={}
for i in range(n):
    s=store[i]
    if s[0] not in dict.keys(): dict[s[0]] = int(s[1])
    else: dict[s[0]]+=int(s[1])
    if dict[s[0]]>=m:
        winner=s[0]
        break
print(winner)
