str1=str(input())
define_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
if str1=='0':
    print(0)
else:
    res=0
    for i in range(0,len(str1)):
        if i==0 or define_dict[str1[i]]<=define_dict[str1[i-1]]:
            res+=define_dict[str1[i]]
        else:                     res+=define_dict[str1[i]]-2*define_dict[str1[i-1]]
    print(res)