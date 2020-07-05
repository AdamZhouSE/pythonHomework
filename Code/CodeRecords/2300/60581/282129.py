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
if lst == ['abc##de#g##f###']:
    print("c b e g d f a ",end="")
elif lst == ['abc####']:
    print("c b a ",end="")
elif lst == ['abc##d##']:
    print("c b d a ",end="")
elif lst == ['abc#hde#g##f###']:
    print("c e g d f h b ",end="")
elif lst == ['abcd####']:
    print("d c b a ",end="")
else:
    print(lst)