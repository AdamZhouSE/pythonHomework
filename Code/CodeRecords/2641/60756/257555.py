s1=''.join(sorted(list(input())))
s2=list(input())
L=len(s1)
for i in range(len(s2)-L):
    if ''.join(sorted(s2[i:i+L]))==s1:
        print(True)
        break
    if i==len(s2)-L-1:
        print(False)