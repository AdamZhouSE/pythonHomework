def solve():
    pass

num=int(input())
list_ans=[]
for i in range(num):
    num=input()
    rats=input().split()
    holes=input().split()
    for i in range(len(rats)):
        rats[i]=int(rats[i])
    for i in range(len(holes)):
        holes[i]=int(holes[i])
    rats.sort()
    holes.sort()
    minus=[]
    for i in range(len(rats)):
        minus.append(abs(int(rats[i])-int(holes[i])))
    minus.sort()
    list_ans.append(minus[-1])
print("\n".join(str(i) for i in list_ans))

