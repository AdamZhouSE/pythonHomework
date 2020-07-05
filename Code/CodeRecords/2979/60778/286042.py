strs=input().split()
lengths=list(map(len,strs))
p=lengths.index(max(lengths))
print(strs[p])