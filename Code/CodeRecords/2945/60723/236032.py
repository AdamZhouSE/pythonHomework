string=input()
number_of_boy=number_of_girl=0
i=-1
while i<len(string)-1:
    i=i+1
    if string[i]=='b':
        if string[i+1]=='o':
            if string[i+2]=='y':
                i=i+1
            i=i+1
        number_of_boy=number_of_boy+1
    elif string[i]=='o':
        if string[i+1]=='y':
            i=i+1
        number_of_boy = number_of_boy + 1
    elif string[i]=='y':
        number_of_boy = number_of_boy + 1
    elif string[i]=='g':
        if string[i+1]=='i':
            if string[i+2]=='r':
                if string[i+3]=='l':
                    i=i+1
                i = i + 1
            i = i + 1
        number_of_girl=number_of_girl+1
    elif string[i]=='i':
        if string[i+1]=='r':
            if string[i+2]=='l':
                i=i+1
            i = i + 1
        number_of_girl=number_of_girl+1
    elif string[i]=='r':
        if string[i+1]=='l':
            i=i+1
        number_of_girl=number_of_girl+1
    elif string[i]=='l':
        number_of_girl=number_of_girl+1
print(number_of_boy)
print(number_of_girl,end='')