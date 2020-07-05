s=input()
s=s[2:len(s)-2]
s=s.split("],[")
left=[]
right=[]
result=[]
for i in range(len(s)):
    string=s[i].split(",")
    left.append(int(string[0]))
    right.append(int(string[1]))
leftremove=[]
rightremove=[]
for i in range(len(left)-1):
    for j in range(i+1,len(left)):
        if right[i]>=left[j]:
            right[i]=right[j]
            leftremove.append(left[j])
            rightremove.append(right[j])
for i in range(len(leftremove)):
    left.remove(leftremove[i])
    right.remove(rightremove[i])
result=[]
for i in range(len(left)):
    seq=[]
    seq.append(left[i])
    seq.append(right[i])
    result.append(seq)
print(result)
