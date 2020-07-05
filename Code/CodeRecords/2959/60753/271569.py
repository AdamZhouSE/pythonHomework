import sys
import re
import math
s=sys.stdin.read()
present=s.split("\n")
s1=present[0]
s2=present[1]
count=0
list1=list(s1)
list2=list(s2)
n1=len(list1)
n2=len(list2)
n=min(n1,n2)
for span in range(1,n+1):
    for i in range(n1-span+1):
        subs1=list1[i:i+span]
        for j in range(n2-span+1):
            subs2=list2[j:j+span]
            if subs1==subs2:
                count+=1
print(count)