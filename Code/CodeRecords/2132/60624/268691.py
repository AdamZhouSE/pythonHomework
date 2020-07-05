def func19():
    s = input()
    n0 = s.count("z")
    n2 = s.count("w")
    n4 = s.count("u")
    n6 = s.count("x")
    n8 = s.count("g")
    n1 = s.count("o")-n0-n2-n4
    n3 = s.count("r")-n0-n4
    n5 = s.count("f")-n4
    n7 = s.count("s")-6
    n9 = s.count("i")-n5-n6-n8
    ns = (n0, n1, n2, n3, n4, n5, n6, n7, n8, n9)
    print("".join((str(i)*n for i, n in enumerate(ns))))
    return
func19()