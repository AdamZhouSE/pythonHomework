num=int(input())
sequence=[]
for m in range(num):
    sequence.append(input().split(" "))
dic={}
max=0
name=""
for i in sequence:
    if i[0] not in dic:
        dic[i[0]]=int(i[1])
    else:
        dic[i[0]]+=int(i[1])
    if dic[i[0]]>max:
        max=dic[i[0]]
        name=i[0]
print(name)
