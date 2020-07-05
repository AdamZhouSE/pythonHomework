n=int(input())
necklace=list(map(int,input().split()))
k=int(input())
for i in range(k):
    type=[]
    question=list(map(int,input().split()))
    for j in range(question[0]-1,question[1]):
        if necklace[j] not in type:
            type.append(necklace[j])
    print(len(type))