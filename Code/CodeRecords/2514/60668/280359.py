if __name__=='__main__':
    s = input()
    t = input()
    point_s = 0
    point_t = 0
    length_s = len(s)
    length_t = len(t)
    while point_t<length_t and point_s<length_s:
        if(s[point_s]==t[point_t]):
            point_s += 1
        point_t+=1
    if(point_s==length_s):
        print("True")
    else:
        print("False")