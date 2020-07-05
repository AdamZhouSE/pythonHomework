#思考：从3->m
n=int(input())
l=list(map(int,input().split()))
outcome="NO"
for c in l:
    sec_c=l[c-1]
    if sec_c!=c:
        third_c=l[sec_c-1]
        if l[third_c-1]==c:
            outcome="YES"
            break
print(outcome)       