import string


def link_words(beginword,endword,dictionary):
    step=1
    real_dic=set(dictionary)
    if endword not in real_dic:
        return 0

    s1,s2 = set([beginword]),set([endword])
    while s1:
        stack = set([])
        real_dic -= s1
        for s in s1:
            for i in range(len(beginword)):
                for j in string.ascii_lowercase:
                    tmp = s[:i] + j + s[i+1:]
                    if tmp not in real_dic:
                        continue
                    if tmp in s2:
                        return step+1
                    stack.add(tmp)

        if len(stack) < len(s2):
            s1=stack
        else:
            s1,s2=s2,stack
        step+=1
    return 0

beginword=input()
endword=input()
dictionary=eval(input())
print(link_words(beginword,endword,dictionary))