def func(s1:str,s2:str):
    before=-1
    for i in s1:
        index=s2.find(i)
        if index<before:
            return False
        else:
            s2.replace(s2[index],'')
            before=index
    return True

print(func(input(),input()))