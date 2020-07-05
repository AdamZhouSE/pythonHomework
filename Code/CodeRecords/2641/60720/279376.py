s1=input()
s2=input()
for i in range(len(s2)-len(s1)+1):
    s=''
    isT=True
    for j in range(i,i+len(s1)):
       s+=s2[j]
    for j in range(len(s1)):
        if s1.count(s1[j])!=s.count(s1[j]):
            isT=False
            break
    if isT:
        print('True')
        break
if not isT:
    print('False')