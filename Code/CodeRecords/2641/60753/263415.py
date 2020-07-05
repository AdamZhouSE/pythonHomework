import sys
import re
import math
s=sys.stdin.read()
lists=s.split("\n")
s1=lists[0]
s2=lists[1]
list1=list(s1)
list1.sort()
list2=list(s2)
n1=len(list1)
n2=len(list2)
if n1>n2:
    print("False")
elif n1==n2:
    if list2.sort()==list1:
        print("True")
    else:
        print("False")
else:
    isTrue=0
    for i in range(n2-n1):
        sublist=list2[i:i+n1]
        sublist.sort()
        if sublist==list1:
            isTrue=1
            break
    if isTrue==1:
        print("True")
    else:
        print("False")
    
