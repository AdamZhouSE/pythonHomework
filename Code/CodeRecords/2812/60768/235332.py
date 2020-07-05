participant=int(input())
scores=input().split(' ')
scores=[int(x) for x in scores]

score=[]
for element in scores:
    if element not in score and element !=0:
        score.append(element)

print (len(score))