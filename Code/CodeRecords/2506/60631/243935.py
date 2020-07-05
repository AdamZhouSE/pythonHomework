inp = input()
li = inp.split(',')
ans = []
for i in range(len(li)):
    str = []
    str.append(li[i])
    for j in range(i+1,len(li)):
        if int(li[j]) >= int(str[len(str)-1]):
            str.append(li[j])
            ans.append(len(str))
if len(ans)==0:
    print(1)
else:
    print(max(ans))