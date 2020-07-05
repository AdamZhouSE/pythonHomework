def str_sort(s=''):
    for i in range(len(s)):
        for j in str_sort(s[0:i] + s[i + 1:]):
            if s[i] + j in s2:
                return 'True'
                break
    else:
        return 'False'



s1=input()
s2=input()
if s1 in s2:
    print('True')
else:
    print(str_sort(s1))
    


    
    