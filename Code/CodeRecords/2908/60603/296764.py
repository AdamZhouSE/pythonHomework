num=int(input())
anslist=[]
for z in range(num):
    string=input()
    string=[i for i in string]
    string.sort()
    string="".join(string)
    if(z==0):
        anslist.append(string)
    else:
        sig=0
        for i in range(len(anslist)):

            if(anslist[i]==string):
                sig=1
                break
        if(sig==0):

            anslist.append(string)
print(len(anslist),end="")
