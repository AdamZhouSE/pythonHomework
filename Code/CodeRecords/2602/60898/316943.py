A = eval(input())
B = eval(input())
max = 0
lenth = 0
row = 0
col = len(A)-1
while row<len(B):
    i = row
    j = col
    lenth = 0
    while i<len(B) and j<len(A):
        if B[i]==A[j]:
            lenth+=1
        else:
            lenth = 0
        if lenth>max:
            max = lenth
        i+=1
        j+=1
    if col>0:
        col-=1
    else:
        row+=1
print(max)
