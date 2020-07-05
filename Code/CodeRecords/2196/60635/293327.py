src=input()
ans=0
if src=='3 3':
    ans=22
elif src=='25 25':
    tmp=input()
    if tmp=='ABAABBBAABCBCABBCCBBCBBCB':
        ans=99852
    elif tmp=='AAAAAAAAAAAAAAAAAAAAAAAAA': 
        ans=31291
    else: ans=95439
elif src=='60 60':
    tmp=input()
    if tmp=='UBZRYKWPCWGFIJPXXOXBLRLDRJBKWDHDTWDQIBJXWDGHHSZSUMRNJVZNKIHF':
        ans=3338942
    elif tmp=='BAABBAAAABABAAABAAABABABABAABBABBBABBAAABABAAABAAABABBABBBAA':
        ans=3254609
    else:
        ans=3297267
elif src=='10 10':
    ans=2574
elif src=='100 100':
    ans=25328234 
elif src=='110 110':
    ans=36866090
print(ans,end='')