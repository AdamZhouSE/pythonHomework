str_in=list(input())
str_copy=str_in.copy()
seq=list(str_in)
seq.sort()
res=""
for i in range(len(seq)):
    res+=str_in[str_copy.index(seq[i])-1]
    str_copy[str_copy.index(seq[i])]="-1"
print(res,end="")