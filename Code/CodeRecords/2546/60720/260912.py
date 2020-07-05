def seq(num):
    if num==0 or num==1 or num==2:
        return 1
    else:
        return seq(num-2)+seq(num-3)
size=int(input())
for i in range(size):
    m=int(input())
    print(seq(m))
