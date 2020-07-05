def is_pre(s1, s2):
    if s2[:len(s1)] == s1:
        return True
    else:
        return False


index= 0
try:
    while True:
        index += 1
        set_01 = []
        while True:
            inp = input()
            if inp == '9':
                break
            set_01.append(inp)
        My_set = sorted(set_01, key=lambda i: len(i))
        has_pre = False
        for i in range(len(My_set)):
            for j in range(i+1, len(My_set)):
                if len(My_set[i]) <= len(My_set[j]):
                    has_pre = is_pre(My_set[i], My_set[j])
                if has_pre:
                    break
            if has_pre:
                break
        if has_pre:
            print("Set %d is not immediately decodable" % index)
        else:
            print("Set %d is immediately decodable" % index)
except EOFError:
    exit()
