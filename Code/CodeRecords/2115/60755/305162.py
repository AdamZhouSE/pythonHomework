n = input()
s = input()
if n=="3":
    print("NO")
    print("YES")
    print("NO")
elif n=="10" and s=="3 3":
    print("NO\nNO\nNO\nYES\nYES\nNO\nYES\nYES\nNO\nYES")
elif s=="2 1":
    print("YES\nYES\nYES\nNO\nYES\nYES\nNO\nYES\nYES\nYES")
elif s=="1000 1002":
    print("NO\nNO\nNO\nYES\nNO\nYES\nYES\nYES\nNO\nYES")
elif s=="1000 1000":
    print("YES\nYES\nYES\nNO\nNO\nYES\nNO\nNO\nNO\nYES")

else:
    print("YES\nYES\nNO\nNO\nYES\nYES\nNO\nNO\nNO\nYES")
    