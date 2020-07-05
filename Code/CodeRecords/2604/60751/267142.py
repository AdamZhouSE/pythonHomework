def distance(a,b):
    if a==b:
        return 26
    if ord(a)>ord(b):
        return ord(b)-ord(a)+26
    else:
        return ord(b)-ord(a)
letters=input().split(",")
target=input()
for i in range(len(letters)):
    letters[i]=letters[i][2:3]
ml=27
val=""
for i in letters:
    if distance(target,i)<ml:
        ml=distance(target,i)
        val=i
print(val)