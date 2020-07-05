num=input().split(' ')
N=int(num[0])
M=int(num[1])
words=[]
for i in range(N):
    words.append(input())
want=[]

for k in range(M):
    temp=input().split(' ')
    temp=[int(x) for x in temp]
    want.append(temp)
def sort(words,want):
    cons=[]
    for i in want:
        temp=words[i[0]-1:i[1]]
        temp.sort(reverse=True)
        cons.append(temp[0])
    return cons
for i in sort(words,want):
    print(i)