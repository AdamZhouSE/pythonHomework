l1=list(input())
l2=list("CODEFESTIVAL2016")
diff=0
for i in range (0,16):
    if l1[i]!=l2[i]:
        diff+=1
print(diff)        