n = int(input())
seq1 = list(map(int,input().split(' ')))
seq2 = list(map(int,input().split(' ')))
punished = [False]*(n+1)

for i in range(1,n+1):
    for j in range(i+1,n+1):
        if seq1.index(i)<seq1.index(j)\
        and seq2.index(i)>seq2.index(j):
            punished[i] = True
        if seq1.index(i)>seq1.index(j)\
        and seq2.index(i)<seq2.index(j):
            punished[j] = True
print(punished.count(True))