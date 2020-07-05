s = input()
s1,s2 = s.split(" ")

judge = True
for i in range(0,len(s1)):
    if s1[i]>s2[i]:
        print(ord(s1[i])-ord(s2[i]))
        judge = False
        break
    else:
        if s1[i]<s2[i]:
            print(ord(s1[i])-ord(s2[i]))
            judge = False
            break
        else:
            continue

if judge:
    print(0)