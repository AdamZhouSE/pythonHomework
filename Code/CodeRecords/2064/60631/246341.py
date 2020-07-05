def tr(one_str):
    define_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if one_str=='0':
        return 0
    else:
        res=0
        for i in range(0,len(one_str)):
            if i==0 or define_dict[one_str[i]]<=define_dict[one_str[i-1]]:
                res+=define_dict[one_str[i]]
            else:    res+=define_dict[one_str[i]]-2*define_dict[one_str[i-1]]
        return res
si = input()
out = tr(si)
print(out)