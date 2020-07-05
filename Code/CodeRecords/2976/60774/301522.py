s = input()
while(True):
    line = input()
    if(line == '}'):
        print('}')
        break
    else:
        line = line.replace(' ','')
        line = line.replace(s,'')
        line = line.replace(s.upper(),'')
        print(line)