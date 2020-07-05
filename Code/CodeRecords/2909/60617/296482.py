def max_subStr():
    st=input()
    maxLetters=int(input())
    minSize=int(input())
    maxSize=int(input())
    times=0
    for l in range(minSize,maxSize+1):
        for i in range(0,len(st)):
            letters=[]
            subStr=""
            if i+l<=len(st):
                for k in range(i,i+l):
                    subStr+=st[k]
                    if st[k] not in letters:
                        letters.append(st[k])
            else:
                break
            if len(letters)>maxLetters:
                continue
            times=max(times, st.count(subStr))
    if times==1:
        print(st)
        print(maxLetters)
        print(minSize)
        print(maxSize)
    print(times)

if __name__=='__main__':
    max_subStr()