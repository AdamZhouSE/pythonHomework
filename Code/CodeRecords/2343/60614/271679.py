init=[int(x) for x in input().split()]
origin=[]
destination=[]
for i in range(init[0]):
    origin.append(list(input()))
for i in range(init[0]):
    destination.append(list(input()))
sequence=''
for i in range(init[0]):
    for j in range(init[1]):
        if origin[i][j]=='o':
            while origin[i][j]!=destination[i][j]:
                if destination[i][j]=='<':
                    sequence+='R'
                    origin[i][j]='<'
                    if origin[i][j+1]=='<':
                        origin[i][j+2]='o'
                        origin[i][j + 1] = '>'
                        j=j+2
                    elif origin[i][j+1]=='n':
                        origin[i+1][j+1]='o'
                        origin[i][j + 1] = '>'
                        i=i+1
                        j=j+1
                    elif origin[i][j+1]=='u':
                        origin[i-1][j+1]='o'
                        origin[i][j + 1] = '>'
                        i=i-1
                        j=j+1
                elif destination[i][j]=='>':
                    sequence+='L'
                    origin[i][j]='>'
                    if origin[i][j-1]=='>':
                        origin[i][j-2]='o'
                        origin[i][j-1] = '<'
                        j=j-2
                    elif origin[i][j-1]=='n':
                        origin[i+1][j-1]='o'
                        origin[i][j-1] = '>'
                        i=i+1
                        j=j-1
                    elif origin[i][j-1]=='u':
                        origin[i-1][j-1]='o'
                        origin[i][j-1] = '>'
                        i=i-1
                        j=j-1
                elif destination[i][j] == 'n':
                    sequence += 'D'
                    origin[i][j] = 'n'
                    if origin[i+1][j] == 'n':
                        origin[i+2][j] = 'o'
                        origin[i+1][j] = 'u'
                        i=i+2
                    elif origin[i+1][j] == '<':
                        origin[i + 1][j + 1] = 'o'
                        origin[i+1][j] = 'u'
                        i = i + 1
                        j = j + 1
                    elif origin[i+1][j] == '>':
                        origin[i + 1][j - 1] = 'o'
                        origin[i+1][j] = 'u'
                        i = i + 1
                        j = j - 1
                elif destination[i][j] == 'u':
                    sequence += 'U'
                    origin[i][j] = 'u'
                    if origin[i-1][j] == 'u':
                        origin[i-2][j] = 'o'
                        origin[i-1][j] = 'n'
                        i=i-2
                    elif origin[i-1][j] == '<':
                        origin[i - 1][j + 1] = 'o'
                        origin[i-1][j] = 'n'
                        i = i - 1
                        j = j + 1
                    elif origin[i-1][j] == '>':
                        origin[i - 1][j - 1] = 'o'
                        origin[i-1][j] = 'n'
                        i = i - 1
                        j = j - 1
            break
print(sequence)