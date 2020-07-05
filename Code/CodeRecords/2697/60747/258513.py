s=input()
s=s[1:len(s)-1].split(",")
root=int(s[0])
a=0
i=1
for j in range(len(s)):
    if s[j]!="null":
        s[j]=int(s[j])
while i<len(s)/2-1:
        if s[s.index(root)*2+1]=='null' or root>int(s[s.index(root)*2+1]):
                if root=="null"or root<int(s[s.index(root)*2+2]) :
                    root = s[i]
                else :
                    print("false")
                    a=-1
                    break
        else:
            print("false")
            a=-1
            break
        i+=1
if a!=-1:
    print("true")