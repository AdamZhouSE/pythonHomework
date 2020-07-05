string=input()
string_dict=list(eval(input()))
string_dict.sort(key=lambda x:-len(x))
index=-1
for i in range(0,len(string_dict)):
    word=string_dict[i]
    list_word=list(word)
    ok=False
    for k in range(0,len(string)):
        if len(list_word)==0:
            ok=True
            break
        if string[k]==list_word[0]:
            list_word.pop(0)
    if ok:
        index=i
        break

if index==-1:
    print('')
else:
    print(string_dict[index])
