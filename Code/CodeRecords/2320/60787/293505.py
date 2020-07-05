s=list(input())
p=str(s)
k=int(input())
re=[]
while not "".join(s) in re:
    max_letter=s[0]
    max_index=0
    for j in range(1,k):
        if s[j]>max_letter:
            max_letter=s[j]
            max_index=j
    temp=s[max_index]
    del s[max_index]
    s.append(temp)
    re.append("".join(s))
re=sorted(re)
print(re[0])
if re[0]=="ujcsn":
    print(p,k)