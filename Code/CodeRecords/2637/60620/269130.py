a=eval(input())
for i in range(1,len(a)-1):
    if(a[:i+1]==sorted(a[:i+1]) and a[i:]==sorted(a[i:],reverse=True)):
        print(i)