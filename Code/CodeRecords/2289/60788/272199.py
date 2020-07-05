from sys import stdin
import sys
def can_be_binary_search_tree_or_not(s):
    if len(s)<=2:
        return True
    else:
        root=s.pop()
        if min(s)>root or max(s)<root:
            return can_be_binary_search_tree_or_not(s)
        for i in range(len(s)):
            if s[i]>root:
                index=i
                break
        m=s[:index]
        n=s[index:]
        if len(m)==0 or len(n)==0:
            return False
        if max(m)<root and min(n)>root:
            return can_be_binary_search_tree_or_not(m) and can_be_binary_search_tree_or_not(n)
        else:
            return False
        
a=int(input().strip())
if a==0 or a==1:
    print("true")
    sys.exit(0)
b=input().strip().split()
s=[int(x) for x in b]
if can_be_binary_search_tree_or_not(s):
    print("true")
else:
    print("false")
