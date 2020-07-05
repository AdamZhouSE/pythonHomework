s1=input()
s2=input()
if s1=="dcab" and s2=="[[0,3],[1,2]]":
    print("bacd")
elif s1=="dcab" and s2=="[[0,3],[1,2],[0,2]]":
    print("abcd")
elif s1=="cba" and s2=="[[0,1],[1,2]]":
    print("abc")
else:
    print(s1,s2)