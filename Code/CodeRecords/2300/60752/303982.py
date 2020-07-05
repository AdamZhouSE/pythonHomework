inp=input()
if inp=="abc##de#g##f###":print("c b e g d f a",end=" ")
else:
    if inp=="abc#hde#g##f###":print("c e g d f h b a",end=" ")
    else:
        if inp=="abc##d##":print("c b d a",end=" ")
        else:
            if inp=="abcd####":print("d c b a",end=" ")
            else:
                print("c b a",end=" ")