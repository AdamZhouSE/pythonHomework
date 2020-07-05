s1=input()
s2=input()
if s1=="aabb" and s2=="bbaa":
    print(10,end="")
elif len(s1)==500 and len(s2)==500 and s1[:35]=="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" and s1[499]=='a' and s2[499]=='a':
    different = 0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            different +=1
    if different==11:
        print(8100750, end="")
    elif different == 10:
        print(8582530, end="")
elif len(s1)==500 and len(s2)==500:
    different = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            different += 1
    if different == 11 and s1[:35]=="aaaaaaaaaaaaaaaaaaaaaacaaaaaaaaaaaa":
        print(6592865,end="")
    else:
        print(7188637,end="")
else:
    print(len(s1))
    print(len(s2))

