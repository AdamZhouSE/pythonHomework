while True:
    n=int(input())
    if n==0:
        break
    else:
        def count(pattern,text):
            i=0
            cnt=0
            while i<len(text):
                if text[i]==pattern[0]:
                    j=i+1
                    start=1
                    flag=True
                    while start<len(pattern) and j<len(text):
                        if pattern[start]!=text[j]:
                            flag=False
                            break
                        start+=1
                        j+=1
                    if start<len(pattern):
                        flag=False
                    if flag:
                        cnt+=1
                i+=1
            return cnt
        patterns=[]
        for i in range(n):
            patterns.append(input())
        text=input()
        idx=0
        times=[]
        for i in range(len(patterns)):
            cnt=count(patterns[i],text)
            times.append((cnt,i))
        times.sort(key=lambda x:x[0],reverse=True)
        largest=times[0][0]
        i=0
        print(largest)
        while times[i][0]==largest and i<len(patterns):
            print(patterns[times[i][1]])
            i+=1

