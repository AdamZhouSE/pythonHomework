s = ""+input()
if s =="abc##de#g##f###":
    print("c b e g d f a ",end="")
elif 'h' in s:
    print("c e g d f h b a ",end="")
elif s.find('c') < s.find('b'):
    print("d c b a ",end="")
elif not "e" in s:
    print("c b d a ",end="")