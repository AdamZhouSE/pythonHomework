l=list(input())
s="CODEFESTIVAL2016"
print(sum([0 if l[i]==s[i] else 1 for i in range(16)]))