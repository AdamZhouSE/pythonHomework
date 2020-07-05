
def judge(s, t):

        if len(s) != len(t):

            return False

        for i in set(s):

            if s.count(i) != t.count(i):

                return False

        return True    

if __name__ == '__main__':
    w=input()
    y=w.split(", ")
    s=y[0][1:]
    t=y[1][1:]
    if judge(s,t):
        print("true")
    else:
        print("false")
    
