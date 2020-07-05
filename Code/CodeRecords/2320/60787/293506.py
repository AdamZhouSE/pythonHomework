s=list(input())
k=int(input())
re=[]
while True:
    max_letter=s[0]
    max_index=0
    for j in range(1,k):
        if s[j]>max_letter:
            max_letter=s[j]
            max_index=j
    temp=s[max_index]
    del s[max_index]
    s.append(temp)
    if "".join(s) in re:
        break
    else:
        re.append("".join(s))
re=sorted(re)
print(re[0])