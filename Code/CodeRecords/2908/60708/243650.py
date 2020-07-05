if __name__ == '__main__':
    i = int(input())#准备输入
    wordlist=[]
    newwordlist=[]
    for n in range(0,i):
        str=input()
        str=str.replace(" ","")
        wordlist.append(str)
    for n in range(0, i):
        str=wordlist[n]
        word=list(str)
        word.sort()
        str=''.join(word)
        newwordlist.append(str)
    newwordlist=list(set(newwordlist))
    result=len(newwordlist)
    print(result,end='')
