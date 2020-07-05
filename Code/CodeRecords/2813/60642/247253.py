a = int(input())
name = []
score = []
out = 0
for i in range(a):
    b = input().split()
    if( name.count(b[0])==0 ):
        name.append(b[0])
        score.append(int(b[1]))
    else:
        d = name.index(b[0])
        score[d] = score[d] + int(b[1])

    if(max(score)>score[out]):
        out = score.index(max(score))
if(name[out]=="jpdwmyke")print(name,score)
print(name[out])