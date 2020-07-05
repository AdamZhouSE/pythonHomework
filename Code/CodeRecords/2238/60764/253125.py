answers=list(map(int,input().split(',')))
rabbit=[]
for i in answers:
    if i not in rabbit:
        rabbit.append(i)
print(len(rabbit)+sum(rabbit))