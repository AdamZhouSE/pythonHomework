num = int(input())
sta = input().split(' ')
des = input().split(' ')
for i in range(0,num):
    sta[i] = int(sta[i])
small = 0
big = 0
if int(des[0])>int(des[1]):
    small = int(des[1])-1
    big = int(des[0])-1
else:
    small = int(des[0])-1
    big = int(des[1])-1
seq = 0
rseq = 0
for i in range(small,big):
    seq+=sta[i]
for i in range(big,num):
    rseq+=sta[i]
for i in range(0,small):
    rseq+=sta[i]
if seq>rseq:
    print(rseq)
else:
    print(seq)