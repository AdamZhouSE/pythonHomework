letters=eval(input())
target=input()
res=chr(ord('z')+1)
if target=='z':
    target=chr(ord('a')-1)
for i in range(len(letters)):
    if ord(letters[i])>ord(target) and ord(letters[i])<ord(res):
        res=letters[i]
if (res=='{'):
    for i in range(len(letters)):
        if ord(letters[i])<ord(res):
            res=letters[i]
print(res)
        