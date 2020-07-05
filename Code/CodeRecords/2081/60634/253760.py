def coutain(word,i,sent):
    for x in word:
        if x != sent[i]:
            return 0
        i += 1
    return 1



A = input()
B = input()

count = 0
i = 0
while i <= len(A) - len(B):
    count += coutain(B,i,A)
    i += 1
    
print(count,end="")

