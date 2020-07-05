import ast
import math
lists = ast.literal_eval(input())

#print(lists)
maxN = 0
maxS = ""
for i in range(lists.__len__()):
    s1 = str(lists[i])
    for j in range(i+1,lists.__len__()):
        s2 = str(lists[j])
        s3 = s1+s2
        s4 = s2+s1
        i1 = int(s3)
        i2 = int(s4)
        bigger = max(i1,i2)
        if(bigger > maxN):
            maxN = bigger
            if (i1 > i2):
                maxS = s3
            else:
                maxS = s4
print(maxS)