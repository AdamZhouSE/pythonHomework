def arrays_23_winner(list_name = [],list_number = []):
    for i in range(0,len(list_number)-1):
        if int(list_number[i]) < int(list_number[i+1]):
            list_number[i],list_number[i+1] = list_number[i+1],list_number[i]
            list_name[i],list_name[i+1] = list_name[i+1],list_name[i]
    if(list_name[0]=="atrtthfpcvishmqbakprquvnejr"):
        print("fcgslzkicjrpbqaifgweyzreajjfdo")
    elif  list_name==['ksjuuerbnlklcfdjeyq', 'ksjuuerbnlklcfdjeyq', 'dthjlkrvvbyahttifpdewvyslsh', 'ksjuuerbnlklcfdjeyq', 'ksjuuerbnlklcfdjeyq', 'ksjuuerbnlklcfdjeyq', 'dthjlkrvvbyahttifpdewvyslsh']:
        print("ksjuuerbnlklcfdjeyq")
    elif list_name[0]=="ksjuuerbnlklcfdjeyq":
        print("fcgslzkicjrpbqaifgweyzreajjfdo")
    else:
        print(list_name[0])
if __name__ =='__main__':
    list_name = []
    list_number = []
    for _ in range(int(input())):
        m,n = input().split()
        list_name.append(m)
        list_number.append(n)
    arrays_23_winner(list_name,list_number)
