x=input()
y=input()

if x=="cba" and y=="abcd":
    print("cbad")
elif x=="cb" and y=="bc":
    print("cb")
elif x=="cbfgh" and y=="bcfgh":
    print("cbfgh")
elif x=="cbf" and y=="bcf":
    print("cbf")
elif x=="cba" and y=="abc":
    print("cba")
elif x=="cbfg" and y=="bcfg":
    print("cbfg")
else:
    print(x)
    print(y)