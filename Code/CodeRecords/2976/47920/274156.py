

str = input()
  
while True:
    try:
        temp = ""
        inp = input()
        inp.replace(str,"")
        if(inp == '\n'):
            print()
        else:
            for i in str:
                for j in inp:
                    if(j != i and j != i.lower() and j != i.upper()):
                        temp = temp + j
            print(temp.replace(' ',''))
    except:
        break