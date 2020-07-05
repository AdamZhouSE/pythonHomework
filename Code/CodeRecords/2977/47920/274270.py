def _reverse(c):  #A 65 Z 90   a 97 z 122
    od = ord(c)
    if(65<=od and od<=90):
        od = 90 - (od-65)
        return chr(od)
    elif(97<=od and od<=122):
        od = 122 - (od - 97)
        return chr(od)
    else:
        return c
#print(_reverse('a'))
while True:
    temp = ""
    inp = input()
    if(inp == "!"):
        break
    else:
        for i in inp:
            temp = temp + _reverse(i)
        print(temp)
            
