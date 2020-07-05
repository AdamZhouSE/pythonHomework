si = input()
li = list(si)
out=0
for i in range(len(li)):
    if li[i]!=li[len(li)-1-i]:
        print('False')
        out=1
        break
if out==0:
    print('True')