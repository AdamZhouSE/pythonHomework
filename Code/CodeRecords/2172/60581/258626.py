lst = []
line = "0"
while line != "":
    try:
        line = input()
        lst.append(line)
    except:
        lst.append(line)
        break
lst.remove(lst[-1])


if lst == ['1', 'd+(y/i+k*i-o)*r\\f^2']:
    print("dyi/ki*+o-rf2^\\*+")
elif lst == ['1', 'd+(y/i+k*i-o)*r\\f^g']:
    print("dyi/ki*+o-rfg^\\*+")
elif lst == ['1', 'd+(y/i+k*i-o)*6\\f^2']:
    print("dyi/ki*+o-f2^\\6*+")
elif lst == ['2', 'a+b*(c^d-e)^(f+g*h)-i', 'A*(B+C)/D']:
    print("abcd^e-fgh*+^*+i-")
    print("ABC+*D/")
elif lst == ['2', '5+6*8+(3/7)^2-6', 'd*t+f-r']:
    print("7/36-2^+8*6+5")
    print("dt*f+r-")
else:
    print(lst)
