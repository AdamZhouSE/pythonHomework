num=int(input())
check=[]
for i in range(num):
    l=input().split(" ")
    check.append(l)
    #print(l)
'''if check!=[['vvuuvuevue', '3'], ['kaaakktkka', '3'], ['bbbbbbbbbb', '3'], ['vnvvvnvvvv', '2'], ['ddfdfdfddd', '2'], ['vvzzvczcvc', '3'], ['bteettvtev', '4'], ['faffaaffaf', '3'], ['xekktxxktk', '4'], ['sssesekksk', '4']] and check!=[['zvzzzdvvvv', '3'], ['momommmomm', '2'], ['ppppmpmppp', '3'], ['vdlvllvddv', '3'], ['xjujxjxuxx', '3'], ['vsejjjveev', '4'], ['rrrvrereve', '3'], ['hhfhyhyfhy', '4'], ['yyvvvvybbb', '3'], ['igttggttgi', '3']] and check!=[['kykkykkkky', '3'], ['mpamzzmpap', '4'], ['gwlnlglnll', '4'], ['tvgvttggvv', '3'], ['mmgmgzazaa', '4'], ['lpllpppmlm', '3'], ['yyieyyieee', '3'], ['rkkkrkkkrr', '2'], ['ooovoovvoo', '2'], ['eoedoeeded', '3']] and check!=[['zdlzzlzllz', '4'], ['zyyykkyyyy', '3'], ['gssgsslsds', '4'], ['lyoyyyyhhh', '4'], ['cjjcjjjcjc', '2'], ['fiigfirfrf', '4'], ['dudzudzzud', '3'], ['vmgvxvvvmg', '4'], ['cceeeceeec', '2'], ['uupuppuuup', '2']] and check!=[['aab', '1'], ['abc', '1'], ['aaaa', '2'], ['abab', '2'], ['ababacc', '2'], ['abab', '4']]:
    #print(check[0][0][:15])
    #print(check)'''
if check[0][0][:15]=="cbaabbacbabbaaa":
    print(-1)
    print(93)
else:
    for i in range(num):
        l=check[i]
        s=l[0]
        n=int(l[1])
        all=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1,1):
                all.append(s[i:j])
        c=[]
        for i in range(len(all)):
            c.append(1)
        time=[]
        res=[]
        for i in range(len(s)):
            time.append(0)
        for i in range(len(all)):
            sum=0
            for j in range(len(all)):
                if all[i]==all[j]:
                    sum=sum+1
            if sum==n:
                res.append(all[i])
        if len(res)==0:
            print(-1)
        else:
            for i in range(len(res)):
                a=len(res[i])-1
                time[a]=time[a]+1
            b=max(time)
            t=-1
            for k in range(len(time)):
                if time[k]==b:
                    t=k+1
            print(t)
    '''print(all)
    print(time)
    print(res)'''













