sentence=input()
search=input()
def has(sentence,search):
    for i in search:
        if i not in sentence:
            return False
    return True
step=len(search)
flag=False
idx=-1
while step<=len(sentence):
    for i in range(0,len(sentence)-step+1):
        if has(sentence[i:i+step],search):
            flag=True
            idx=i
            break
    if flag:
        break
    step+=1
if idx==-1:
    print("")
else:
    print(sentence[idx:idx+step])