n = int(input())
arrayQ = [int(i) for i in input().split(" ")]
length = 1
for i in range(n):
    questions = []
    lastQ = arrayQ[i]
    questions.append(lastQ)
    for j in range(i+1,n):
        if arrayQ[j]>lastQ and arrayQ[j]<=2*lastQ:
            lastQ = arrayQ[j]
            questions.append(lastQ)
            #print(questions)
    length= max(length,len(questions))
print(length)

