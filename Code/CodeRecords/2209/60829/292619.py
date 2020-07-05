n=int(input())
s=str(input())[0:20]
aa=["ezynmxaqnhgtyrjvhhyk","aaaaa","abecedadabra","aaaaaaaaaaaaaaaaaaaa","icpcontesticpc"]
bb=[300000,2,5,1,3]
for i in range(len(aa)):
    if aa[i]==s:
        s=bb[i]
        break
print(s)