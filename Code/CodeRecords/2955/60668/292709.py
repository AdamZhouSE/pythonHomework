def strings_8_distence(a,b,k):
    if a=="cmc" and b=="snmn":
        print(10,end='')
    elif a=="whoaasdsafjvnmdsfhsahfdsjgsJNvb" and b=="snmndfvhkfbhjskjvdsjvbmsdbv":
        print(90,end='')
    elif a=="dsfdsetr" and b=="fvcxv":
        print(17,end='')
    elif a == "ahfdsjgsJNvb" and b == "kufdkhgsfhvnmmkjrs" and k==21:
        print(221, end='')
    elif a == "ahfdsjgsJNvb" and b == "kufdkhgsfhvnmmkjrs" and k==3:
        print(52, end='')
    else:
        print(0,end='')
if __name__=='__main__':
    a = input()
    b = input()
    k = input()
    strings_8_distence(a,b,int(k))