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
            times=max(times, cal_times(subStr,st))
    print(times)

def cal_times(subStr,st):
    count=0
    length=len(subStr)
    start=0
    while start+length<=len(st):
        start=st.find(subStr)
        if start!=-1:
            start=start+length
            count+=1
        else:
            return count
    return count

if __name__=='__main__':
    max_subStr()

if __name__=='__main__':
    max_subStr()