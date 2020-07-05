s1=input()
s2=input()
head=0
for i in range(len(s2)):
    #print(head)
    if s2[i]==s1[head]:
        head=head+1
# print(head)
# print(len(s1)-1)
if head==len(s1):
    print(True)
else:
    print(False)
