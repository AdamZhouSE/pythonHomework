questions=int(input())
for i in range(questions):
    init=input()
    sequence1=[int(x) for x in input().split()]
    sequence2=[int(x) for x in input().split()]
    result=[0]*(len(sequence1)+len(sequence2))
    for j in range(len(sequence1)):
        for k in range(len(sequence2)):
            result[j+k]=sequence1[j]*sequence2[k]
    print(" ".join(result))