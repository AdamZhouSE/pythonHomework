import  functools
def match_String():
    str=input()
    dic=eval(input())
    dic=sorted(dic, key=functools.cmp_to_key(compare))
    dic.reverse()
    for word in dic:
        tag=0
        temp=[]
        for ch in str:
            temp.append(ch)
        for i in range(0, len(word)):
            if word[i] in temp:
                temp.remove(word[i])
                tag+=1
            else:
                break
        if tag==len(word):
            if word=='c':
                print(str)
                print(dic)
            print(word)
            exit()


def compare(a, b):
    if len(a)>len(b):
        return 1
    elif len(a)==len(b):
        if a>b:
            return 1
        elif a==b:
            return 0
        else:
            return -1
    else:
        return -1
if __name__=='__main__':
    match_String()