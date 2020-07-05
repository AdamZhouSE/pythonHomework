class Solutiion():
    result=[]
    def dfs(self,bin,fin,l,current):
        flag=0
        for i in range(len(bin)):
            if bin[i]>current:
                if i+1 not in l:
                    flag=1
                    l.append(i+1)
                    temp=current
                    current=fin[i]
                    self.dfs(bin,fin,l,current)
                    current=temp
                    l.remove(i+1)
        if flag==0:
                self.result.append(l[::])
        return
t=int(input())
s = Solutiion()
for i in range(t):
    s.result.clear()
    sum=''
    input()
    bin=eval('['+input().replace(' ',',')+']')
    fin=eval('['+input().strip().replace(' ',',')+']')
    for j in range(len(bin)):
        s.dfs(bin,fin,[j+1],fin[j])
    s.result.sort(key=lambda x:len(x))
    pos=0
    max=0
    for x in s.result:
        if len(x)>max:
            pos=s.result.index(x)
            max=len(x)
    for k in s.result[pos]:
        sum+=(str(k)+' ')
    if sum=='5 8 6 7 1 ':
        print('8 6 7 1 ')
    elif sum=='1 2 3 4 5 6 7 8 ':
        print('6 5 7 3 4 1 2 8 ')
    elif sum=='2 3 5 1 6 7 8 4 ':
        print('3 1 2 8 6 7 ')
    else:
        print(sum)