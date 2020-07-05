num = int(input())
k=int(input())
def cal_set(n,k):
    factor=1
    seq=[]

    output=''
    for count in range(1, n+1):
        seq.append(count)
        factor=factor*count
    k=k-1
    while count>1:
        factor = factor // count
        output=output+str(seq.pop(k//factor))     #select and pop
        k=k%factor
        count=count-1
    output=output+str(seq[0])

    return output

print(cal_set(num,k))

