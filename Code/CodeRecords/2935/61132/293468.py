l=list(input())
print(sum([l[:i].count("Q")*l[i+1:].count("Q")for i in range(len(l)) if l[i]=="A"]),end='')