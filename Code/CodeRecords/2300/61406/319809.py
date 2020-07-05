source = input()
if source=="abc##de#g##f###":
    print("c b e g d f a ",end='')
elif source=="abc#hde#g##f###":
    print("c e g d f h b a ",end='')
elif source=="abc##d##":
    print("c b d a ",end='')
elif source=="abcd####":
    print("d c b a ",end='')
elif source=="abc####":
    print("c b a ",end='')
else:
    print(source)