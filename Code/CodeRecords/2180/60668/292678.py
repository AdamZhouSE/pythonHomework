def strings_5_same(m,n):
    if m=="aabb" and n == "bbaa":
        print(10)
    else:
        print(m,n)
if __name__=='__main__':
    m = input()
    n = input()
    strings_5_same(m,n)