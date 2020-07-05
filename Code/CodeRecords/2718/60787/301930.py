s=list(input())
op=eval(input())
count=0
for i in range(1,len(s)):
    count+=i
i=0
while i<len(op):
    j=0
    while j<len(op):
        if not i==j:
            if op[i][0]==op[j][0] and (not op[i][1]==op[j][1]) and (not sorted([op[i][1],op[j][1]]) in op):
                op.append(sorted([op[i][1],op[j][1]]))
            elif op[i][0]==op[j][1] and (not op[i][1]==op[j][0]) and (not sorted([op[i][1],op[j][0]]) in op):
                op.append(sorted([op[i][1],op[j][0]]))
            elif op[i][1]==op[j][0] and (not op[i][0]==op[j][1]) and (not sorted([op[i][0],op[j][1]]) in op):
                op.append(sorted([op[i][0],op[j][1]]))
            elif op[i][1]==op[j][1] and (not op[i][0]==op[j][0]) and (not sorted([op[i][0],op[j][0]]) in op):
                op.append(sorted([op[i][0],op[j][0]]))
        j+=1
    i+=1
for k in range(0,len(s)):
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            if s[i]>s[j] and [i,j] in op:
                s[i],s[j]=s[j],s[i]
print("".join(s))